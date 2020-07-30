import boto3

def lambda_handler(event, context):
    s3_console = boto3.resource('s3')
    for each_bucker in s3_console.buckets.all():
        print(each_bucker.name)
    
    return None