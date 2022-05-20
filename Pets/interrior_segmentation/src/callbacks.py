import tensorflow as tf


def keras_callback():
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath='../models/checkpoint.h5',
        monitor='val_dice',
        mode='max',
        save_best_only=True)

    return model_checkpoint_callback
