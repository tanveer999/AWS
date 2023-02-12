import boto3

ses = boto3.client('ses')

body = """
Hi Tanveer,
This is a test mail.
This is a test mail.
"""

ses.send_email(
    Source  = 'tanveerahmed1811226@gmail.com',
    Destination = {
        'ToAddresses': [
            'tanveerahmed1811226@gmail.com'
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

