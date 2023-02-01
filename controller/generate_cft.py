import boto3


def create_cloudformation_stack(params):
    try:
        session = boto3.Session(profile_name='admin', region_name='us-east-1')
        client = session.client('cloudformation')

        parameters = []

        keys = params.keys()

        for key in keys:
            parameters.append({'ParameterKey': key,
                               'ParameterValue': params[key],
                               'UsePreviousValue': False
                               })

        response = client.create_stack(
            StackName='s3-bucket-creation',
            TemplateURL='https://demobucket1151.s3.ap-south-1.amazonaws.com/s3_bucket.yaml',
            Parameters=parameters,
            DisableRollback=False,
            TimeoutInMinutes=123,
            Capabilities=[
                'CAPABILITY_NAMED_IAM',
            ],
        )
        return response['StackId']

    except Exception as e:
        print(e)
        return e
