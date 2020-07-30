import boto3

def lambda_handler(event, context):

    sns_client=boto3.client('sns',"ap-south-1")
    sns_client.publish(TargetArn="arn:aws:sns:ap-south-1:208508730742:avi_lambda_automatic_state_change", Message="run ec2 is stopped")
    
    return None