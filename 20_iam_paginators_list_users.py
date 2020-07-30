import boto3

def lambda_handler(event, context):
    iam_users=boto3.client('iam')
    paginator=iam_users.get_paginator('list_users')

    count=0
    for pages in paginator.paginate():
        for users in pages['Users']:
            print(users['UserName'])
            count +=1
    print('total data in each page',len(pages['Users']))
    print('total users => ',count)
    
    return None