import boto3

def lambda_handler(event, context):
    
    s3_con_res=boto3.resource('s3')
    for buckets in s3_con_res.buckets.all():
        print(buckets.name)
    print(" ")
    s3_con_cli=boto3.client('s3')
    for each_buckets in s3_con_cli.list_buckets()['Buckets']:
        print(each_buckets['Name'])