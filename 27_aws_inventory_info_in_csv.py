import boto3
import csv
from datetime import datetime
aws_console = boto3.session.Session(profile_name='default')
ec2_con = aws_console.resource(service_name='ec2', region_name='ap-south-1')
count = 1
csv_object = open("21_inventory_info.csv", "w", newline="")
writer = csv.writer(csv_object)
writer.writerow(["Serial No.", "Instance Ids.", "Instance Type",
                 "Architecture", "LaunchTime", "Private_Ips"])
for each in ec2_con.instances.all():
    # print(dir(each))
    writer.writerow([count, each.instance_id, each.instance_type, each.architecture,
                     each.launch_time.strftime('%d/%M/%Y'), each.private_ip_address])
    count += 1
