from model import unet

from load_data import load_data
from show_prediction import predict
from callbacks import keras_callback


train_gen, val_gen, x_test, y_test = load_data(datapath='../data/processed/')

if __name__ == '__main__':
    model = unet()
    model.summary()

    model.fit(
        train_gen,
        epochs=100,
        validation_data=val_gen,
        callbacks=[keras_callback()]
    )
    model.save('../models/checkpoint.h5')
    predict(model, x_test, y_test)
