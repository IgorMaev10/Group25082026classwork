import boto3
import config

s3client = boto3.client(
    service_name='s3',
    region_name=config.AWS_REGION_NAME,
    endpoint_url=config.AWS_ENDPOINT_URL,
    aws_access_key_id=config.AWS_ACCESS_KEY,
    aws_secret_access_key=config.AWS_SECRET_KEY,
)

target_file_name = 'Ihor_Maiev.html'
s3client.upload_file("Ihor_Maiev.html", config.AWS_BUCKET_NAME, target_file_name)
public_url = f"{config.AWS_PUBLIC_URL}/{target_file_name}"
print(public_url)
