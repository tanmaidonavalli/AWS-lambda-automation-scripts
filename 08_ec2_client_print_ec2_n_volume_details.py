import boto3
from pprint import pprint

def lambda_handler(event, context):
    ec2_console=boto3.client('ec2',region_name='ap-south-1')
    resource=ec2_console.describe_instances()['Reservations']
    print("\tInstance Id \t Instance Image Id  \t Launch time \t state")
    for each_item in resource:
        for instance in each_item['Instances']:
            print(instance['InstanceId'],'\t', instance['ImageId'],'\t', instance['LaunchTime'].strftime("%d-%m-%Y"),'\t', instance['State']['Name'])
    print('\n')

    response=ec2_console.describe_volumes()['Volumes']
    for i in response:
        for j in i['Attachments']:
            print('volume id is',j['VolumeId'],' AZ is',i['AvailabilityZone'] )
        
    return None