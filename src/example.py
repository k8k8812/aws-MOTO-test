import boto3, boto 
from boto3 import session

# client: low-level service access
# resource: higher-level object-oriented service access; 

s3_client = boto3.client('s3',verify=False)
s3_conn = boto.connect_s3(is_secure=False) # this has solved ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
# s3_resource = boto3.resource('s3',)
bucket_prefix = 'yingsbucket-python-aws'

def create_bucket(bucket_prefix, s3_connection):
    generated_session = session.Session()
    current_region = generated_session.region_name
    bucket_name = bucket_prefix.join("01")
    bucket_response = s3_connection.create_bucket(bucket_name)
    print(bucket_name, current_region)
    return bucket_name, bucket_response

name, bucket_response = create_bucket(bucket_prefix=bucket_prefix, s3_connection=s3_conn)






