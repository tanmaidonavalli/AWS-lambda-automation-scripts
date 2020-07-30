import boto3
from random import random
import sys

def get_iam_client_object():
    iam_console=boto3.client("iam")
    return iam_console

def main():
    iam_client=get_iam_client_object()
    iam_user_name = "avinash_singh12"
    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] == "EntityAlreadyExists":
            print(f"UserName Already present with name {iam_user_name}")
            sys.exit()
        else:
            print(f"please verify following error and try again {e}")
            sys.exit()
    response=iam_client.create_access_key(UserName=iam_user_name)
    print(f"UserName is   => {iam_user_name}")
    print(f"Access key is => {response['AccessKey']['AccessKeyId']}")
    print(f"Secret key is => {response['AccessKey']['SecretAccessKey']}")
    iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=PolicyArn)

    return None

if __name__ == "__main__":
    main()