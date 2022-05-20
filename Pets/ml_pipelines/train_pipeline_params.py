import yaml
from dataclasses import dataclass
from marshmallow_dataclass import class_schema


@dataclass
class Model:
    type: str
    save_folder: str
    model_filename: str
    metrics_filename: str
    params: dict


# @dataclass
# class S3Params:
#     endpoint_url: str
#     aws_access_key_id: str
#     aws_secret_access_key: str
#     data_path: str
#     bucket_name: str


@dataclass
class TrainingPipelineParams:
    input_source_data: str
    splitting_val_size: float
    model: Model
    # s3: S3Params


TrainingPipelineParamsScheme = class_schema(TrainingPipelineParams)


def read_config(config_path: str):
    with open(config_path) as f:
        scheme = TrainingPipelineParamsScheme()
        return scheme.load(yaml.safe_load(f))
