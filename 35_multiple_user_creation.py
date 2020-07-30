import csv
import boto3
import sys
from random import choice


def get_iam_client_object():
    iam_console = boto3.client("iam")
    return iam_console


def get_random_password():
    len_of_password = 8
    valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-"
    password = []
    for each_char in range(len_of_password):
        password.append(choice(valid_chars_for_password))
    random_password = "".join(password)
    return random_password


def main():

    iam_client = get_iam_client_object()
    fo = open("IAM.csv", 'r')
    data = csv.reader(fo)
    next(data)
    if not data:
        sys.exit()
    for each in data:

        try:
            print(f"sno. {each[0]}   '{each[1]}' ")
            iam_user_name = each[1]
            Programatic_Access = each[2]
            Console_Access = each[3]
            PolicyArn = each[4]
            skip = False
            try:
                user_id = iam_client.create_user(UserName=iam_user_name)
                print(f"IAM UserName is => {iam_user_name}")
                print("Account Id is   =>", user_id["User"]["Arn"][13:25])
            except Exception as e:
                if e.response['Error']['Code'] == "EntityAlreadyExists":
                    print(
                        f"UserName Already present with name {iam_user_name}\n")
                    skip = True
                else:
                    print(f"please verify following error and try again {e}")
                    sys.exit()

            if skip == True:
                continue

            if Console_Access == "Yes":
                ######################### giving management console access #############
                iam_user_password = get_random_password()
                iam_client.create_login_profile(
                    UserName=iam_user_name, Password=iam_user_password)
                print(f"Password is     => {iam_user_password}")

            if Programatic_Access == "Yes":
                #################### giving programatic access ##############
                response = iam_client.create_access_key(UserName=iam_user_name)
                print(
                    f"Access key is   => {response['AccessKey']['AccessKeyId']}")
                print(
                    f"Secret key is   => {response['AccessKey']['SecretAccessKey']}")

            # ######################## attaching administrative access policy  #################
            if PolicyArn == "None":
                pass
            else:
                iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn=PolicyArn)
                

        except Exception as e:
            print("please fill all columns,or write 'None' , further details are :",e)
    
        print("\n")



if __name__ == "__main__":
    main()
