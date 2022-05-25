import os
from pathlib import Path

import numpy as np

from datagen import CarOrTruckGenerator


def load_data(walkpath):
    train_paths, train_targets = [], []
    val_paths, val_targets = [], []
    test_paths, test_targets = [], []

    for dirpath, _, filenames in os.walk(walkpath):
        for file in filenames:
            path = Path(dirpath).joinpath(file)

            if 'train' in str(path.parent):
                train_paths.append(str(path))
                train_targets.append(str(path.parent.name))
            elif 'valid' in str(path.parent):
                val_paths.append(str(path))
                val_targets.append(str(path.parent.name))
            else:
                test_paths.append(str(path))
                test_targets.append(str(path.parent.name))

    train_gen = CarOrTruckGenerator(np.asarray(train_paths), np.asarray(train_targets), batch_size=32)
    val_gen = CarOrTruckGenerator(np.asarray(val_paths), np.asarray(val_targets), batch_size=32)
    test_gen = CarOrTruckGenerator(np.asarray(test_paths), np.asarray(test_targets), batch_size=32)

    del train_paths, train_targets, val_paths, val_targets, test_paths, test_targets

    return train_gen, val_gen, test_gen