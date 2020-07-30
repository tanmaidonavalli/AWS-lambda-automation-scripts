import boto3

def lambda_handler(event, context):
    source_region = 'ap-south-1'
    destination_region = 'ap-southeast-1'
    
    ec2_client_source = boto3.client('ec2', source_region)
    all_snapshots = []
    sts_client = boto3.client('sts')
    account_id = sts_client.get_caller_identity().get('Account')
    f1 = {'Name': 'tag:backup', 'Values': ['yes']}
    for each_snapshot in ec2_client_source.describe_snapshots(OwnerIds=[account_id], Filters=[f1])['Snapshots']:
        all_snapshots.append(each_snapshot['SnapshotId'])
    
    ec2_client_destination = boto3.client('ec2', destination_region)
    waiter = ec2_client_destination.get_waiter('snapshot_completed')
    for each_snapshot in all_snapshots:
        ec2_client_destination.copy_snapshot(Description=f"this snapshot is copied from {source_region} for disastor recovery",SourceRegion=source_region,SourceSnapshotId=each_snapshot,TagSpecifications=[{'ResourceType': 'snapshot','Tags': [{'Key': 'backup_from_region', 'Value': source_region}]}])
        print(f'snapshot completed for {each_snapshot} , now deleting its old tag and creating new one')
        
        ec2_client_source.delete_tags(Resources=[each_snapshot],Tags=[{'Key': 'backup','Value': 'yes' }])
            
        ec2_client_source.create_tags(Resources=[each_snapshot],Tags=[{'Key': 'backup','Value': 'completed'}])
