import boto3

def lambda_handler(event, context):
    s3_console=boto3.client('s3')
    bucket_name='temp-2612'
    paginator=s3_console.get_paginator('list_objects')
    for pages in paginator.paginate(Bucket=bucket_name):
        for items in pages['Contents']:
            print(items['Key'])
    return None