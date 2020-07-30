import boto3
from pprint import pprint

def lambda_handler(event, context):
    ec2_con_cli=boto3.client(service_name='ec2')
    waiter=ec2_con_cli.get_waiter('instance_running')
    
    all_instance=[]
    f1={"Name":"tag:Type", "Values":['ubuntu','suse']}
    for each in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
        for new in each['Instances']:
            all_instance.append(new['InstanceId'])
    print('starting instance with ids ',all_instance)
    ec2_con_cli.start_instances(InstanceIds=all_instance)
    waiter.wait(InstanceIds=all_instance)
    print("your instance is up and running")
    
    return None