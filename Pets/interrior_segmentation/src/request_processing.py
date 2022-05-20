import io
import base64
from PIL import Image

import numpy as np


def decoding(base64_image):
    base64_decoded = base64.b64decode(base64_image)

    image = Image.open(io.BytesIO(base64_decoded))
    shape = np.asarray(image).shape
    processed = np.asarray(image.resize((256, 256), resample=Image.BICUBIC)) / 255

    return processed, shape


def encoding(mask, shape):
    mask = (np.squeeze(mask) * 255).astype(np.uint8)
    resized = Image.fromarray(mask).resize(tuple(shape[-2::-1]), resample=Image.BICUBIC)

    buffer = io.BytesIO()
    resized.save(buffer, format='PNG')

    return base64.b64encode(buffer.getvalue())
