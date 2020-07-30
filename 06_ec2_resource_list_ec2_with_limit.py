import boto3

def lambda_handler(event, context):
    ec2_console=boto3.resource('ec2')
    ec2_resource=ec2_console.instances.limit(1)
    for instance in ec2_resource:
        print(instance.id)
        
    return None