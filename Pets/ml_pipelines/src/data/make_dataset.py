import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from boto3 import resource
from botocore.client import Config
# from train_pipeline_params import S3Params


# def download_data(input_source_data: str, s3_params: S3Params) -> None:
#     s3 = resource('s3',
#                   endpoint_url=s3_params.endpoint_url,
#                   aws_access_key_id=s3_params.aws_access_key_id,
#                   aws_secret_access_key=s3_params.aws_secret_access_key,
#                   config=Config(signature_version='s3v4'),
#                   region_name='us-east-1')
#
#     s3.Bucket(s3_params.bucket_name).download_file(s3_params.data_path, input_source_data)


def read_data(path: str):
    df = pd.read_csv(path)
    if df.columns[0] == 'Unnamed: 0':
        return pd.read_csv(path, index_col=0)
    return df


def preprocess_data(df):
    encode_cols = ['ChestPain', 'Thal', 'AHD']
    df[encode_cols] = df[encode_cols].apply(preprocessing.LabelEncoder().fit_transform)
    df.dropna(axis=0, inplace=True)
    return df


def split_train_test_split(df, val_size):
    train_df, val_df = train_test_split(df, test_size=val_size)
    return train_df, val_df


def get_features_target(df: pd.DataFrame, target_column: str):
    target = df[target_column]
    features = df.drop(target_column, axis=1)
    return features, target
