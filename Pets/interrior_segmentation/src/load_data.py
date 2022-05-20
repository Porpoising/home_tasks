import os
from pathlib import Path

import numpy as np

from typing import List

from sklearn.model_selection import train_test_split

from datagen import ImageGenerator


def load_data(datapath: str):
    image_paths, mask_paths = [], []

    for dirpath, _, filename in os.walk(datapath):
        for file in filename:
            path = Path(dirpath).joinpath(file)
            if path.parent.name == 'images':
                image_paths.append(str(path))
            else:
                mask_paths.append(str(path))

    image_paths = np.asarray(image_paths)
    mask_paths = np.asarray(mask_paths)

    x_train, x_test, y_train, y_test = train_test_split(image_paths, mask_paths, train_size=0.8)
    x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, train_size=0.5)

    del mask_paths
    del image_paths

    train_gen = ImageGenerator(x_train, y_train, 'train_gen', batch_size=4)
    val_gen = ImageGenerator(x_val, y_val, 'val_gen', batch_size=4)

    return train_gen, val_gen, x_test, y_test


# if __name__ == '__main__':
#     print(x_train[0], y_train[0])
# print(x_val[0], y_val[0])
# print(x_test[0], y_test[0])
