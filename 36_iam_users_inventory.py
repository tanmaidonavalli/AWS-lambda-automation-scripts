import boto3
import csv
import time
iam_console = boto3.client('iam')
sno = 1

csv_object = open("IAM_Inventory.csv", "w", newline="")
writer = csv.writer(csv_object)
writer.writerow(["Serial No.", "IAM_User_Name","User_ID", "User ARN", "User Creation Date","Attached Policies","Groups associated"])


for each_user in iam_console.list_users()['Users']:
    iam_user_name = each_user['UserName']
    iam_user_ID = each_user['UserId']
    iam_user_Arn = each_user['Arn']
    iam_user_creation_date = each_user['CreateDate'].strftime("%d-%m-%Y %H:%M")

    if iam_console.list_groups_for_user(UserName=iam_user_name)['Groups']:
        group=""
        for each in iam_console.list_groups_for_user(UserName=iam_user_name)['Groups']:
            group="\n" + each['GroupName'] + group
        user_groups= group[1:]
    else:
        user_groups="None"

    if iam_console.list_attached_user_policies(UserName=iam_user_name)['AttachedPolicies']:
        arn = ""
        for each_policy in iam_console.list_attached_user_policies(UserName=iam_user_name)['AttachedPolicies']:
            arn= "\n" +each_policy['PolicyName'] +arn
        policy_attached = arn[1:]
    else:
        policy_attached = " None "

    writer.writerow([sno, iam_user_name, iam_user_ID, iam_user_Arn,iam_user_creation_date, policy_attached,user_groups])
    print(sno, iam_user_name, iam_user_ID, iam_user_Arn, iam_user_creation_date,policy_attached,user_groups)

    sno += 1
