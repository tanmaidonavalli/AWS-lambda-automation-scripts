import boto3

def lambda_handler(event, context):
    ec2_console=boto3.client('ec2')
    response2=ec2_console.describe_instances()['Reservations']
    print("Ec2 instance ids are")
    for each_ec2 in response2:
        for ec2_id in each_ec2['Instances']:
            print(ec2_id['InstanceId'])

    return None