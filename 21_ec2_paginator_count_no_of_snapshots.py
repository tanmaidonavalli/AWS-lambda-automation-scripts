import boto3

def lambda_handler(event, context):
    
    ec2_user=boto3.client('ec2')
    paginator=ec2_user.get_paginator('describe_snapshots')
    count=0
    for each_pages in paginator.paginate():
        for snapshots in each_pages['Snapshots']:
            count += 1
    print(count)

    return None