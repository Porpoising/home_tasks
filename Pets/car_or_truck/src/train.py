from model import cot_raw

from load_data import load_data
from callbacks import keras_callback

train_gen, val_gen, test_gen = load_data(walkpath='../data/raw/')

if __name__ == '__main__':
    model = cot_raw()
    model.summary()

    model.fit(
        train_gen,
        epochs=300,
        validation_data=val_gen,
        callbacks=[keras_callback()]
    )
    model.save('../models/cot_raw/checkpoint.h5')
