import cv2
import numpy as np
import os
from pathlib import Path


def get_image_paths_array(images_path):
    images_path_list = []
    for dirpath, _, filenames in os.walk(images_path):
        for file in filenames:
            path = Path(dirpath).joinpath(file)
            images_path_list.append(path)

    return np.asarray(images_path_list)


def
