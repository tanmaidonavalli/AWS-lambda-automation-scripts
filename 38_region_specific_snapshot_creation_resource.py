import boto3
from pprint import pprint
ec2_console = boto3.resource('ec2', 'ap-south-1')

f1 = {"Name": "tag:prod", "Values": ["backup"]}
volumes = ec2_console.volumes.filter(Filters=[f1])
all_volumes = []
for each in volumes:
    all_volumes.append(each.id)

waiter = ec2_console.meta.client.get_waiter("snapshot_completed")

for each_volume in all_volumes:
    response = ec2_console.create_snapshot(
        Description="created by boto3 script",
        VolumeId=each_volume,
        TagSpecifications=[{
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'snapshot of {each_volume}'}]}])
    waiter.wait(SnapshotIds=[response.id])
    print(f"snapshot of '{each_volume}' is => {response.id}")
