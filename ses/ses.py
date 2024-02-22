import boto3

ses = boto3.client('ses')

body = """
Hi Tanveer,
This is a test mail.
This is a test mail.
"""

ses.send_email(
    Source  = '',
    Destination = {
        'ToAddresses': [
            ''
        ]
    },
    Message = {
        'Subject': {
            'Data': 'SES Test',
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': body,
                'Charset': 'UTF-8'
            }
        }
    }
)

