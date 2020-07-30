import boto3

def lambda_handler(event, context):
    ec2_resource = boto3.resource('ec2')
    my_instance_object = ec2_resource.Instance("i-03454c58b1d97e20b")
    if my_instance_object.state['Name'] == "running":
        print(f"Instance is already running")
    else:
        print("starting the instance... ")
        my_instance_object.start()
        my_instance_object.wait_until_running()
        print("instance is up and running")

    return None
