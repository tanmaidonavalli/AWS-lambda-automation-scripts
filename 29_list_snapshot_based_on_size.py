import boto3

def lambda_handler(event, context):
    ec2_con=boto3.resource(service_name='ec2',region_name='ap-south-1')
    sts_man_console=boto3.client(service_name='sts')
    resource=sts_man_console.get_caller_identity()
    f={"Name":"volume-size","Values":["8"]} #enter size we want in gb
    for each in ec2_con.snapshots.filter(Filters=[f],OwnerIds=[resource.get('Account')]):
        print(each.id)
    return None