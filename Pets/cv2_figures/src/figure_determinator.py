import os
import logging
import sys
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI


from processing import process_and_predict, decoding

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

app = FastAPI()


class PredictionModel(BaseModel):
    image: str


@app.on_event('startup')
async def load_data():
    logger.info('Session started successful')


@app.get('/')
def read_root():
    return 'Entry point here'


@app.get('/predict', response_model=str)
def show_image(request: PredictionModel):
    logger.info('Predicting data')

    base64_image = request.image
    logger.info(f'base64_image: {base64_image}')
    image_decoded = decoding(base64_image)

    return process_and_predict(image_decoded)


if __name__ == '__main__':
    uvicorn.run('figure_determinator:app', host='0.0.0.0', port=int(os.getenv('PORT', 8000)), workers=5, reload=True)
