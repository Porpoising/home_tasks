import tensorflow as tf
from tensorflow import keras
from keras import layers

from typing import Tuple

from losses import dice, mse_log_dice


def convolution(x, filters: int, dropout: float = 0.3, iterations: int = 2):
    for _ in range(iterations):
        x = layers.Conv2D(filters, kernel_size=3, padding='same')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation("relu")(x)
        if dropout > 0:
            x = layers.Dropout(dropout)(x)

    return x


def upsample(x, filters: int, layer):
    x = layers.Conv2DTranspose(filters, kernel_size=3, strides=2, padding='same')(x)
    x = layers.concatenate([x, layer])
    x = layers.Dropout(0.3)(x)
    x = convolution(x, filters)

    return x


def downsample(x, filters: int):
    prev = convolution(x, filters)
    x = layers.MaxPooling2D(strides=2)(prev)
    x = layers.Dropout(0.3)(x)

    return prev, x


def unet(shape: Tuple = (256, 256, 3),
         learning_rate=0.001,
         num_layers: int = 3,
         filters=32) -> tf.keras.Model:
    input = layers.Input(shape=shape)
    x = input

    residuals = []
    for _ in range(num_layers):
        residual, x = downsample(x, filters=filters)
        residuals.append(residual)
        filters *= 2

    # conv_256, x = downsample(x, filters=32)
    # conv_128, x = downsample(x, filters=64)
    # conv_64, x = downsample(x, filters=128)
    # conv_32, x = downsample(x, filters=256)
    # conv_16, x = downsample(x, filters=512)

    x = convolution(x, filters=filters, dropout=0)

    # x = upsample(x, filters=512, layer=conv_16)
    # x = upsample(x, filters=256, layer=conv_32)
    # x = upsample(x, filters=128, layer=conv_64)
    # x = upsample(x, filters=64, layer=conv_128)
    # x = upsample(x, filters=32, layer=conv_256)

    for residual in reversed(residuals):
        filters //= 2
        x = upsample(x, filters=filters, layer=residual)

    output1 = layers.Conv2D(filters=1, kernel_size=3, strides=1, padding='same', activation='sigmoid')(x)
    output2 = layers.Conv2D(filters=1, kernel_size=3, strides=1, padding='same', activation='sigmoid')(x)
    output3 = layers.Conv2D(filters=1, kernel_size=3, strides=1, padding='same', activation='sigmoid')(x)

    final = layers.concatenate([output1, output2, output3])

    print('out1 shape:', tf.shape(output1),
          'out2 shape:', tf.shape(output2),
          'out3 shape:', tf.shape(output3),
          'final shape:', tf.shape(final), sep='\n')

    model = tf.keras.Model(inputs=input, outputs=final, name='U-Net')

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate),
        loss=mse_log_dice,
        metrics=[dice],
    )
    return model


if __name__ == '__main__':
    model = unet()
    model.summary()
