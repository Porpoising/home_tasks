import tensorflow as tf
from tensorflow import keras
from keras import layers

from typing import Tuple


def convolution(x, filters: int, dropout: bool = True):
    x = layers.Conv2D(filters=filters, kernel_size=3, padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation('relu')(x)
    if dropout:
        x = layers.Dropout(0.3)(x)

    return x


def augmentations(x):
    x = layers.RandomFlip("horizontal")(x)
    x = layers.RandomRotation(0.2)(x)

    return x


def cot_raw(shape: Tuple = (128, 128, 3),
            learning_rate=0.001) -> tf.keras.Model:
    input = layers.Input(shape=shape)
    x = augmentations(input)

    for filters in [32, 48, 64, 80]:
        if filters == 80:
            x = convolution(x, filters=filters, dropout=False)
        else:
            x = convolution(x, filters=filters)

    x = layers.Flatten()(x)
    output = layers.Dense(1, activation='sigmoid')(x)

    model = tf.keras.Model(inputs=input, outputs=output, name='CarOrTruckRaw')
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy'],
    )
    return model
