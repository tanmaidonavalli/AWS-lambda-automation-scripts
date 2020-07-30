import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    all_regions = []
    for region in ec2_client.describe_regions()['Regions']:
        all_regions.append(region['RegionName'])
        
    for each_region in all_regions:
        ec2_client = boto3.client('ec2',each_region)
        ebs_volumes = []
        f1 = {'Name': 'tag:prod', 'Values': ['backup']}
        paginator = ec2_client.get_paginator("describe_volumes")
        for each_page in paginator.paginate(Filters=[f1]):
            for each_volume in each_page['Volumes']:
                ebs_volumes.append(each_volume['VolumeId'])
        
        if bool(ebs_volumes) == True:
            print(f"\n############ Working on {each_region} ##############")
            for each_volume in ebs_volumes:
                print(f"taking snapshot of {each_volume} | ", end="")
                
                response = ec2_client.create_snapshot(
                Description="this snapshot is taken by lambda and cloudwatch",
                VolumeId=each_volume,
                TagSpecifications=[{
                        'ResourceType': 'snapshot',
                        'Tags':[{
                                            'Key': 'backup',
                                            'Value': 'yes'  }]  }])
                waiter = ec2_client.get_waiter('snapshot_completed')
                waiter.wait(SnapshotIds=[response.get('SnapshotId')])
                print(f"[DONE] | snapshot id is {response['SnapshotId']}")
            ebs_volumes.clear()