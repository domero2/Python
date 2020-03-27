from boto3.session import Session
import boto3

access_key = 'zz'
secret_key = 'zz'
bucket_name = 'zz'

session = Session(aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)
s3session = session.resource('s3')
your_bucket = s3session.Bucket(bucket_name)

s3 = boto3.client('s3')

for s3_file in your_bucket.objects.all():
    s3.download_file(bucket_name, s3_file, 'FILE_NAME')
    
    

