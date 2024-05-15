import boto3
from boto3.s3.transfer import TransferConfig
import os
import threading
import sys

def mpu(bucket_name, filepath, bucket_key):
    config = TransferConfig(multipart_threshold=100, 
                        max_concurrency=10,
                        multipart_chunksize=100,
                        use_threads=True)
    
    s3.upload_file(filepath, bucket_name, bucket_key,Config=config,Callback=ProgressPercentage(filepath))
    

class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()

if __name__ == '__main__':
    s3 = boto3.client('s3')

    bucket_name = os.getenv('AWS_DEPLOYMENT_S3')
    filepath = 'file.txt'
    bucket_key = f'mpu/{filepath}'
    mpu(bucket_name,filepath,bucket_key)
