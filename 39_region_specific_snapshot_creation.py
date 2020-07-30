import boto3
from pprint import pprint
ec2_client = boto3.client('ec2', 'ap-south-1')

def lambda_handler(event, context):
    f1 = {'Name': 'tag:prod', 'Values': ['backup']}
    ebs_volumes = []
    paginator = ec2_client.get_paginator("describe_volumes")
    for each_page in paginator.paginate(Filters=[f1]):
        for each_volume in each_page['Volumes']:
            ebs_volumes.append(each_volume['VolumeId'])

    for each_volume in ebs_volumes:
        print(f"[DONE] | snapshot of {each_volume} ",end="")
        response = ec2_client.create_snapshot(
            Description="this snapshot is taken by lamda and cloudwatch",
            VolumeId=each_volume,
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                                    'Tags':
                                    [{
                                        'Key': 'delete_on',
                                        'Value': '90'
                                    }]
                }]
        )
        waiter = ec2_client.get_waiter('snapshot_completed')
        waiter.wait(
            SnapshotIds=[response.get('SnapshotId')]
        )
        print(f"is =>  {response['SnapshotId']}")