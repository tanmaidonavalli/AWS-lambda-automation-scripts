import boto3

def lambda_handler(event, context):
    s3_console=boto3.client('s3')
    bucket_name='temp-2612'

    all_objects=s3_console.list_objects(Bucket=bucket_name)
    for files in all_objects['Contents']:
        print(files['Key'])
        