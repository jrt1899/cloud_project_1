import boto3
import sys

s3 = boto3.client(
        "s3"
)

file = sys.argv[1]

image = s3.upload_file(file, "project-1-input-images", file)
