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