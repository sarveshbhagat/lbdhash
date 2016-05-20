from __future__ import print_function
import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image
import dhash
import hashlib

s3_client = boto3.client('s3')

def handler(event, context):
    #for record in event['Records']:
        #bucket = record['s3']['bucket']['name']
        #key = record['s3']['object']['key']

    bucket = 'kellanio-alestic-lambda-example'
    key = 'iceberg.jpg'
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
    upload_path = '/tmp/resized-{}'.format(key)

    s3_client.download_file(bucket, key, download_path)
    image = Image.open(download_path)
    image_dhash = dhash.dhash(image)
    image_sha256 = hashlib.sha256(open(download_path, 'rb').read()).hexdigest()

    return {'sha256': image_sha256, 'dhash': image_dhash}