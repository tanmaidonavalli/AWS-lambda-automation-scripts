import boto3

def lambda_handler(event, context):
    ec2_client=boto3.client('ec2')
    client_waiter_object=ec2_client.get_waiter("instance_stopped")
    print("stopping the instance... ")
    ec2_client.stop_instances(InstanceIds=['i-03454c58b1d97e20b'])
    client_waiter_object.wait(InstanceIds=["i-03454c58b1d97e20b"])
    print("instance is stopped ")

    return None