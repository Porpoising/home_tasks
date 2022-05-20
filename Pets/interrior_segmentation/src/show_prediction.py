import numpy as np

from PIL import Image

import tensorflow as tf

from load_data import load_data


def predict(model, x_test, y_test):
    for _ in range(len(x_test)):
        img = Image.open(x_test[_])
        mask = np.asarray(Image.open(y_test[_]))
        shape = np.asarray(img).shape

        resized = np.asarray(img.resize((256, 256), resample=Image.BICUBIC)) / 255
        prediction = model.predict(np.array([resized]))

        prediction = (np.squeeze(prediction) * 255).astype(np.uint8)
        prediction = np.asarray(Image.fromarray(prediction).resize(tuple(shape[-2::-1]), resample=Image.BICUBIC))

        concatenated = np.hstack((np.asarray(img), mask, prediction))
        concatenated = Image.fromarray(concatenated)

        concatenated.save(f'../data/predicted/image+mask+predicted_{_}.jpg')


# if __name__ == '__main__':
#     model = tf.keras.models.load_model('../models/checkpoint.h5', compile=False)
#     model.load_weights('../models/w-50-0.56.h5')
#
#     _, _, x_test, y_test = load_data(datapath='../data/processed/')
#     predict(model, x_test, y_test)