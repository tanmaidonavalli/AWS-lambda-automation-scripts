import boto3

def lambda_handler(event, context):
    ec2_client=boto3.client('ec2')
    ec2_resource=boto3.resource('ec2')
    my_instance_object=ec2_resource.Instance("i-03454c58b1d97e20b")
    
    print("starting the instance... ")
    my_instance_object.start()
    
    client_waiter_object=ec2_client.get_waiter("instance_running")
    client_waiter_object.wait(InstanceIds=["i-03454c58b1d97e20b"])
    print("instance is up and running")

    return None
    