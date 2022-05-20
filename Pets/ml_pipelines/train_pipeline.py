# some comment just to create pull request
import logging
import sys

import click

from src.models.model_fit_predict import train_model, predict_model, eval_model, serialize_model, save_metrics
from src.data.make_dataset import read_data, preprocess_data, split_train_test_split, get_features_target  # download_data
from train_pipeline_params import read_config, TrainingPipelineParams

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


def train_pipeline(params: TrainingPipelineParams):
    # logger.info('Downloading data from S3')
    # download_data(params.input_source_data, params.s3)

    logger.info('Reading data')
    input_data = read_data(params.input_source_data)

    logger.info('Preprocessing data')
    data = preprocess_data(input_data)
    logger.info(f'Data shape {data.shape}')

    # train_features, train_target = get_features_target(train_df)
    # val_features, val_target = get_features_target(val_df)

    logger.info('Data splitting')
    train_df, val_df = split_train_test_split(data, params.splitting_val_size)
    logger.info(f'train_df shape {train_df.shape}')
    logger.info(f'val_df shape {val_df.shape}')

    train_features, train_target = get_features_target(train_df, 'AHD')
    val_features, val_target = get_features_target(val_df, 'AHD')

    model_config = params.model
    logger.info(f'Training with model config: {model_config}')
    model = train_model(train_features, train_target, model_config)

    logger.info('Making predictions on validation data')
    predict = predict_model(model, val_features)
    logger.info('Calculating metrics')
    metrics = eval_model(predict, val_target)
    logger.info(f'Metrics {metrics}')

    logger.info('Saving metrics')
    save_metrics(metrics, model_config.save_folder, model_config.metrics_filename)

    logger.info('Saving model')
    serialize_model(model, model_config.save_folder, model_config.model_filename)


@click.command(name='train_pipeline')
@click.argument('config_path')
def train_pipeline_command(config_path: str):
    params = read_config(config_path)
    logger.info(f'config_path {config_path}')
    train_pipeline(params)


if __name__ == '__main__':
    train_pipeline_command()
