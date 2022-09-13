from unittest import mock
import pytest 
from boto3 import session 
import boto3
from moto import mock_s3
from src.s3_bucket_main import *
from jproperties import Properties

bucket_param = "baobao-cutiepie-11"

pytest.fixture
def aws_configs():
    configs = Properties()
    with open('/Users/A.G.C/Documents/drafts/pyProjectMoto/credentials.config', 'rb') as config_file:
        configs.load(configs)
    return configs

# pytest.fixture
# def s3_client():
#     boto3.client('s3', bucket_name=bucket_param, aws_access_key_id=aws_configs['aws_access_key_id'].data, aws_secret_access_key=aws_configs['aws_secret_access_key'].data)


def test_s3_creation():
    assert create_s3_bucket(bucket_name=bucket_param) == True

@mock_s3
def test_s3_upload():
    upload = upload_to_s3_bucket(file_path="aaa")
    assert upload == True

