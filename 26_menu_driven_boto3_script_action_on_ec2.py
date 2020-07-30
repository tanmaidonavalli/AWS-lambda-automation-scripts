import boto3
import sys
amc = boto3.session.Session(profile_name="default")
ec2_client = amc.client("ec2")
ec2_resource = amc.resource("ec2")

while True:
    print("This script perform following actions on ec2 instance")
    print("""
          1. Start
          2. Stop
          3. Terminate
          4. Exit
    """)
    opt = int(input("Enter your option "))
    
    if opt == 1:
        instance_id = input("Enter your ec2 instance id  ")
        instance_object = ec2_resource.Instance(instance_id)
        instance_object.start()
        print('##### done #####\n')

    elif opt == 2:
        instance_id = input("Enter your ec2 instance id  ")
        ec2_client.stop_instances(InstanceIds=[instance_id])
        print('##### done #####\n')

    elif opt == 3:
        instance_id = input("Enter your ec2 instance id for terminating ")
        instance_object = ec2_resource.Instance(instance_id)
        instance_object.terminate()
        print('##### done #####\n')

    else:
        print("than you this script is working, even i am surprised")
        sys.exit()

