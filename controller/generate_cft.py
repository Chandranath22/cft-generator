import json
import boto3


def create_cloudformation_stack(params):
    try:
        session = boto3.Session(profile_name='admin', region_name='us-east-1')
        client = session.client('cloudformation')

        parameters = []

        keys = params['params'].keys()

        for key in keys:
            parameters.append({'ParameterKey': key,
                               'ParameterValue': params['params'][key],
                               'UsePreviousValue': False
                               })

        response = client.create_stack(
            StackName=params['stack-name'],
            TemplateURL='https://cf-templates-poc-dev.s3.amazonaws.com/s3/s3_bucket.yaml',
            Parameters=parameters,
            DisableRollback=False,
            TimeoutInMinutes=123,
            Capabilities=[
                'CAPABILITY_NAMED_IAM',
            ],
        )
        return response['StackId']

    except Exception as e:
        return f"Something went wrong--{e}"
