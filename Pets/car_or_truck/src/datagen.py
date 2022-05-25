import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import math
import numpy as np

from PIL import Image


encoder = LabelEncoder()


class CarOrTruckGenerator(keras.utils.Sequence):
    def __init__(self, x, y, batch_size):
        self.x, self.y = x, y
        self.batch_size = batch_size

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_x = [np.asarray(Image.open(path)) for path in batch_x]
        batch_x = np.asarray(batch_x, dtype=np.float32) / 255

        batch_y = encoder.fit_transform(batch_y).reshape(-1, 1)

        return batch_x, batch_y

    def on_epoch_end(self):
        indices = np.random.permutation(len(self.x))
        self.x, self.y = self.x[indices], self.y[indices]
