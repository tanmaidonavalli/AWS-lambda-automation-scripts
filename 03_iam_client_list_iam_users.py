import boto3

def lambda_handler(event, context):
    iam_users_client=boto3.client(service_name='iam')
    for each in iam_users_client.list_users()['Users']:
        print(each['UserName'])
        
    return None