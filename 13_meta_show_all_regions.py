import boto3

def lambda_handler(event, context):
    ec2_console=boto3.resource('ec2')
    for region in ec2_console.meta.client.describe_regions()['Regions']:
        print(region['RegionName'])

    return None