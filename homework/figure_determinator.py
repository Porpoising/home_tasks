import cv2
import numpy as np
import os
from pathlib import Path


def get_image_paths_array(images_path: str):  # getting all paths of images into one array
    images_path_list = []
    for dirpath, _, filenames in os.walk(images_path):
        for file in filenames:
            path = Path(dirpath).joinpath(file)
            images_path_list.append(str(path))

    return images_path_list


# def contours_processing(contour):
#     convex_hull = cv2.convexHull(contour)
#     perimeter = cv2.arcLength(convex_hull, True)
#     approximated = cv2.approxPolyDP(convex_hull, 0.004 * perimeter, True)


def figure_determination(poly):
    if len(poly) == 3:
        return 'triangle'
    elif len(poly) == 4:
        return 'rectangle'
    else:
        return 'circle'


def process(path):  # image processing and showing
    image_grayscale = cv2.imread(path, 0)  # reading in grayscale mode
    image_mask = cv2.Canny(image_grayscale, 125, 125)
    image_contours, _ = cv2.findContours(image_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    convex_hull = cv2.convexHull(image_contours[0])
    perimeter = cv2.arcLength(convex_hull, True)
    approximated = cv2.approxPolyDP(convex_hull, 0.03 * perimeter, True)
    figure_name = figure_determination(approximated)
    return figure_name, image_mask


def image_showing(figure_name, image_grayscale):
    cv2.imshow(f'{figure_name}', image_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path = 'C:/Users/nowic/Desktop/imgs/'  # path to folder with images
    images_paths = get_image_paths_array(path)
    for path in images_paths:
        fig, image = process(path)
        image_showing(fig, image)
