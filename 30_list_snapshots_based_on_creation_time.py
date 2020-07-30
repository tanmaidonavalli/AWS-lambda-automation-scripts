import boto3
import datetime

def lambda_handler(event, context):
    ec2_con=boto3.resource(service_name='ec2',region_name='ap-south-1')
    sts_man_console=boto3.client(service_name='sts')
    resource=sts_man_console.get_caller_identity()

    #It will fetch today date
    today=datetime.datetime.now()
    print(today)
    #it will take time that by that we want our snapshot time match
    # it will convert time into string for comparing, the time of snapshot creating that we want to filter 

    # filter_time=str(datetime.datetime(today.year,today.month,today.day,16,23,33))
    filter_time=str(datetime.datetime(2020,7,15,16,23,33))
    print(filter_time)
    for each in ec2_con.snapshots.filter(OwnerIds=[resource.get('Account')]):
        if each.start_time.strftime("%Y-%m-%d %H:%M:%S")==filter_time:
            print(each.id)

    return None