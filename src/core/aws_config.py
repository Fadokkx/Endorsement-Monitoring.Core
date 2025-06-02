import boto3
import os
from dotenv import load_dotenv

load_dotenv()

class ConfigAws:
    Aws_client = boto3.client('s3', 
                    aws_access_key_id= os.getenv("AWS_ACESS_KEY"), 
                    aws_secret_access_key= os.getenv("AWS_SECRET_KEY"))

class Paths:
    Bucket = os.getenv("AWS_BUCKET")
    Diretorio = os.getenv("AWS_DIRECTORY")