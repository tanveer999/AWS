import boto3
import json
from botocore.exceptions import ClientError

def get_lambda_configuration(function_name):
    output = []
    response = lambda_client.get_function_configuration(FunctionName=function_name)

    output.append(
        {
            'function_name': response.get('FunctionName', ''),
            'vpc_config': response.get('VpcConfig', '')
        }
    )
    return output

def get_lambda_policy(function_name):
    output = []
    try:
        response = lambda_client.get_policy(FunctionName=function_name)
    except ClientError as err:
        response = ''
    print(json.dumps(response))

if __name__ == '__main__':
    lambda_client = boto3.client('lambda', region_name='ap-south-1')
    # print(json.dumps(get_lambda_configuration('python-rest-api-dev-hello')))

    get_lambda_policy('python-rest-api-dev-hello')