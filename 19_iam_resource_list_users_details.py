import boto3
import datetime

def lambda_handler(event, context):
    iam_console_resource=boto3.resource(service_name='iam')
    user_resource=iam_console_resource.users.all()
    for resource in user_resource:
        print(' ')
        print(f'--------------------- {resource.user_name} --------------------------')
        print(resource.user_name,resource.arn,resource.user_id, resource.create_date.strftime("%Y-%m-%d"))
    return None