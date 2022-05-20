import os
import logging
import sys

import numpy as np
import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel
import tensorflow as tf

from request_processing import decoding, encoding

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

app = FastAPI()
model = None


class PredictionModel(BaseModel):
    image: str


@app.on_event('startup')
async def app_load():
    logger.info('Loading model...')
    global model
    model = tf.keras.models.load_model('../models/checkpoint.h5', compile=False)

    logger.info('Session started successful')


@app.get('/')
async def entry():
    print('Entry point here')


@app.get('/predict', response_model=str)
async def make_prediction(request: PredictionModel):
    logger.info('Receiving base64 image...')
    data = request.image

    logger.info('Decoding image...')
    image, shape = decoding(data)

    logger.info('Making a prediction...')
    prediction = model.predict(np.array([image]))

    logger.info('Encoding to base64...')

    return encoding(prediction, shape)


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=int(os.getenv('PORT', 8000)), workers=5, reload=True)
