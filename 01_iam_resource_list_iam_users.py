import boto3

def lambda_handler(event, context):
    iam_console=boto3.resource('iam')
    for each_user in iam_console.users.all():
        print(each_user.name)
    
    return None