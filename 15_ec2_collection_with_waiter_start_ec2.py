import boto3

def lambda_handler(event, context):
    ec2_console=boto3.resource('ec2')
    ec2_waiter=boto3.client('ec2')
    waiter=ec2_waiter.get_waiter('instance_running')


    all_instance=[]
    for each in ec2_console.instances.all():
        all_instance.append(each.id)

    ec2_console.instances.start()
    waiter.wait(InstanceIds=all_instance)
    print("all instance are up and running")
    
    return None