import os
from dotenv import load_dotenv

load_dotenv()

HOST=os.environ.get("HOST")
PORT=os.environ.get("PORT")
USERNAME=os.environ.get("REDIS_USERNAME")
PASSWORD=os.environ.get("PASSWORD")

AWS_REGION_NAME=os.environ.get("AWS_REGION_NAME")
AWS_ENDPOINT_URL=os.environ.get("AWS_ENDPOINT_URL")
AWS_ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY=os.environ.get("AWS_SECRET_KEY")
AWS_PUBLIC_URL=os.environ.get("AWS_PUBLIC_URL")
AWS_BUCKET_NAME=os.environ.get("AWS_BUCKET_NAME")
