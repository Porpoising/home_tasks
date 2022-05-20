import tensorflow as tf


def dice(y_true, y_pred):
    y_true_c = tf.keras.backend.flatten(y_true)
    y_pred_c = tf.keras.backend.flatten(y_pred)
    intersection = tf.keras.backend.sum(y_true_c * y_pred_c, axis=-1)
    return (2. * intersection + tf.keras.backend.epsilon()) / (
            tf.keras.backend.sum(y_true_c, axis=-1) +
            tf.keras.backend.sum(y_pred_c, axis=-1) +
            tf.keras.backend.epsilon())
    # intersection = tf.keras.backend.sum(y_true * y_pred, axis=[1, 2, 3])
    # union = tf.keras.backend.sum(y_true, axis=[1, 2, 3]) \
    #         + tf.keras.backend.sum(y_pred, axis=[1, 2, 3])
    #
    # return tf.keras.backend.mean((2 * intersection + tf.keras.backend.epsilon()) /
    #                              (union + tf.keras.backend.epsilon()), axis=0)


def mse_log_dice(y_true, y_pred):
    mse_walls = tf.keras.losses.mean_squared_error(y_true, y_pred)
    dice_walls = tf.keras.backend.log(dice(y_true, y_pred))
    return mse_walls - dice_walls
