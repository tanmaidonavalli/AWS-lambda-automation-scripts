import boto3

def lambda_handler(event, context):
    s3_console=boto3.client('s3')
    response3=s3_console.list_buckets()
    for bucket in response3['Buckets']:
        print(bucket['Name'])

    return None