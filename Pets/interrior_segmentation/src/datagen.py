from tensorflow import keras

import numpy as np
import math

from PIL import Image


class ImageGenerator(keras.utils.Sequence):
    def __init__(self, x, y, name: str, batch_size: int = 32):
        self.x, self.y = np.asarray(x), np.asarray(y)
        self.name = name
        self.batch_size = batch_size

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        batch_x = [np.asarray(Image.open(path).resize((256, 256), resample=Image.BICUBIC)) for path in batch_x]
        batch_x = np.asarray(batch_x, dtype=np.float32) / 255

        batch_y = [np.asarray(Image.open(path).resize((256, 256), resample=Image.BICUBIC)) for path in batch_y]
        batch_y = np.asarray(batch_y, dtype=np.float32) / 255

        return batch_x, batch_y

    def on_epoch_end(self):
        indices = np.random.permutation(len(self.x))
        self.x, self.y = self.x[indices], self.y[indices]
