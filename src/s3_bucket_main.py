import boto
from boto3 import session, client
from botocore.exceptions import ClientError
from pathlib import Path
from jproperties import Properties

def init_config():
    configs = Properties()
    with open('/Users/A.G.C/Documents/drafts/pyProjectMoto/credentials.config', 'rb') as config_file:
        configs.load(config_file)
        # id = configs['aws_access_key_id'].data
        # secret = configs['aws_secret_access_key'].data
    file_PATH= str(Path(__file__).absolute().parent.parent) + "/resource/helloWorld.txt" 
    s3_bucket_name = "baobao-cutiepie-11"
    
    # return file_PATH, s3_bucket_name, id, secret
    return file_PATH, s3_bucket_name


# def create_s3_bucket(bucket_name, id, secret):
# def create_s3_bucket(bucket_name, aws_configs):
def create_s3_bucket(bucket_name):
    try:
        s3_session = session.Session()
        # s3_client = client('s3', use_ssl=False, aws_access_key_id=aws_configs['aws_access_key_id'].data, aws_secret_access_key=aws_configs['aws_secret_access_key'].data)
        s3_client = client('s3', use_ssl=False)
        response = s3_client.create_bucket( ACL='public-read-write', Bucket=bucket_name,
        # reateBucketConfiguration={'LocationConstraint': 'us-east-2'},
        # GrantFullControl='string',
        # GrantRead='string',
        # GrantReadACP='string',
        # GrantWrite='string',
        # GrantWriteACP='string',
        ObjectLockEnabledForBucket=True|False, ObjectOwnership='BucketOwnerPreferred')
        return True
          
    except ClientError as e:
        print(e)
        return False
    return 


def download_from_s3_bucket():
    pass 

def upload_to_s3_bucket(file_path):
    return False

# path, bucket_name, id, secret = init_config()
path, bucket_name= init_config()
# create_s3_bucket(bucket_name=bucket_name, id=id, secret=secret)
create_s3_bucket(bucket_name=bucket_name)

