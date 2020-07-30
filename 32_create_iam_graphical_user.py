import boto3
from random import choice
import sys

def get_iam_client_object():
    session=boto3.session.Session(profile_name='default')
    iam_client=session.client('iam')
    return iam_client

def get_random_password():
    len_of_password=8
    valid_chars_for_password="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-"
    password=[]
    for each_char in range(len_of_password):
        password.append(choice(valid_chars_for_password))
    random_password = "".join(password)
    return random_password

def main():
    #calling function to create client object
    iam_client=get_iam_client_object()
    iam_user_name="avinash_singh17"
    iam_user_password=get_random_password()
    # now we have to decide which iam policy we want to attach, go to console and copy arn
    iam_policy_arn='arn:aws:iam::aws:policy/AdministratorAccess'

    # to create user, can get error if user already exists
    try:
        a=iam_client.create_user(UserName=iam_user_name)
        print("Account ID is ",a['User']['Arn'][13:25])
    except Exception as e:
        if e.response["Error"]["Code"]=='EntityAlreadyExists':
            print("Iam user already exists with name",iam_user_name)
            sys.exit() 
        else:
            print("please look at this error",e)

    # to create its login profile
    iam_client.create_login_profile(UserName=iam_user_name,Password=iam_user_password,PasswordResetRequired=False)

    # to attach policy to newly created iam user
    iam_client.attach_user_policy(UserName=iam_user_name,PolicyArn=iam_policy_arn)

    print(f"UserName => {iam_user_name}")
    print(f"Password => {iam_user_password}")

    return None

if __name__ == "__main__":
    main()