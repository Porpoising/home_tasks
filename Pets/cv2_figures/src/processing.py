import cv2
import base64
import numpy as np


def decoding(base64_image):
    base64_decoded = base64.b64decode(base64_image)

    im_arr = np.frombuffer(base64_decoded, dtype=np.uint8)  # im_arr is one-dim Numpy array
    image = cv2.imdecode(im_arr, flags=cv2.IMREAD_GRAYSCALE)

    # image = np.array([image_np])
    return image


def figure_determination(poly):
    if len(poly) == 3:
        return 'triangle'
    elif len(poly) == 4:
        return 'rectangle'
    else:
        return 'circle'


def process_and_predict(image):  # image processing and showing
    image_mask = cv2.Canny(image, 125, 125)
    image_contours, _ = cv2.findContours(image_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    convex_hull = cv2.convexHull(image_contours[0])
    perimeter = cv2.arcLength(convex_hull, True)

    poly = cv2.approxPolyDP(convex_hull, 0.03 * perimeter, True)
    figure_name = figure_determination(poly)

    return figure_name
