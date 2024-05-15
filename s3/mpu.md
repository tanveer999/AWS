#### Multi part upload lifecycle policy for aborting failed uploads

a. Policy
```
{
    "Rules": [
        {
            "ID": "Test Rule",
            "Status": "Enabled",
            "Filter": {
                "Prefix": ""
            },
            "AbortIncompleteMultipartUpload": {
                "DaysAfterInitiation": 7
            }
        }
    ]
}
```

b. Apply policy
```
aws s3api put-bucket-lifecycle-configuration   \
--bucket DOC-EXAMPLE-BUCKET1  \
--lifecycle-configuration file://lifecycle.json
```


### Ref:
1. https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-upload-object.html
2. https://medium.com/analytics-vidhya/aws-s3-multipart-upload-download-using-boto3-python-sdk-2dedb0945f11
3. https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html