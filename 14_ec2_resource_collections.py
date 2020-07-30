import boto3

def lambda_handler(event, context):
    ec2_console = boto3.resource('ec2')

    for each in ec2_console.instances.all():
        print(each.id)

    print("......................")

    for each in ec2_console.instances.limit(1):
        print(each.id)

    print("......................")

    f1 = {'Name': 'instance-state-name', 'Values': ['running']}
    f2 = {'Name': 'instance-type', 'Values': ['t2.micro']}
    for each in ec2_console.instances.filter(Filters=[f1, f2]):
        print(each.id)

    return None
