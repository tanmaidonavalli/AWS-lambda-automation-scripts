import boto3

def lambda_handler(event, context):
    s3_console=boto3.resource('s3')
    bucket_name='temp-2612'
    bucket_console=s3_console.Bucket(bucket_name)
    for items in bucket_console.objects.all(): #here we can apply filters
        print(items.key)
    
    return None