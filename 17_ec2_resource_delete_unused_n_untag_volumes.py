import boto3
from pprint import pprint

def lambda_handler(event, context):
    ec2_con_res=boto3.resource('ec2', region_name='ap-south-1')
    f={"Name":"status","Values":['available']}
    available_ebs=[]
    resource=ec2_con_res.volumes.filter(Filters=[f])
    for each_volume in resource:
        if not each_volume.tags: # if there are no tags then
            available_ebs.append(each_volume.id)
            each_volume.delete()
    print("deleting used and untag volumes",available_ebs)
    
    return None