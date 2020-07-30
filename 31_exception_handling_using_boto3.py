import sys 
'''
try:
	import boto3
except Exception as e:
	print(e)
'''
try:
	import boto3
	import botocore # are boto3 is build on top of botocore and it has all exceptions, instaled with boto3
except ModuleNotFoundError:
	print("Boto3 is not installed. Please intall boto3 and try againg")
	sys.exit(1)
except Exception as e:
	print(e)
	sys.exit(2)

try:
	aws_mag_con=boto3.session.Session(profile_name="ec2-developer") # root
except botocore.exceptions.ProfileNotFound:
	print("root profile is not configured on your .aws credential file. Use other profile or please configure root profile")
	sys.exit(3)
except Exception as e:
	print(e)
	sys.exit(4)

try:
	iam_con_re=aws_mag_con.resource(service_name="iam")
	for each_user in iam_con_re.users.all():
		print(each_user)
except botocore.exceptions.ClientError as e:
	if e.response['Error']['Code'] == "AccessDenied":
		print("Your profile is not having access to work with IAM Users")
	else:
		print(e.response['Error']['Code'])
		sys.exit(5)
except Exception as e:
	print(e)
	sys.exit(6)