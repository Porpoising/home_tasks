import tensorflow as tf


def keras_callback():
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath='../artifacts/w-{epoch:02d}-{val_loss:.2f}.h5',
        save_weights_only=True,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)

    return model_checkpoint_callback
