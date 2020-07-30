import boto3

def lambda_handler(event, context):
    # aws=boto3.session.Session(profile_name='educate')
    sts_man_console=boto3.client(service_name='sts')
    resource=sts_man_console.get_caller_identity()
    print(f"Default, User id => {resource.get('UserId')}   account id => {resource.get('Account')} ")
        
    return None