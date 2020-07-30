import boto3
from pprint import pprint

def lambda_handler(event, context):
    ec2_con_cli=boto3.client('ec2', region_name='ap-south-1')
    f={"Name":"status","Values":['available']}
    available_ebs=[]
    resource=ec2_con_cli.describe_volumes()['Volumes']
    for i in resource:
    # print(i)
        if not "Tags" in i and i['State']=='available': # we are trying to print volume which nave no tags
            ec2_con_cli.delete_volume(VolumeId=i['VolumeId'])
            print("deleting volume having id",i['VolumeId'])
    
    return None