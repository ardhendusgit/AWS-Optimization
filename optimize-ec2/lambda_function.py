import json
import boto3

def getvolumeid(volume_arn):
    arn_parts = volume_arn.split(':') # split the json response
    volume_id = arn_parts[-1].split('/')[-1] # get the volume id
    return volume_id

def lambda_handler(event, context):
  
    volume_arn = event['resources'][0] # the json would essentially be received in event so we parse the event json
    volume_id = getvolumeid(volume_arn)
    
    ec2_client = boto3.client('ec2')

    # easily available in the boto3 documentation
    response = ec2_client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3'
    )

    # if for some reason we're using a function URL
    return {
        'statusCode': 200,
        'body': json.dumps('EC2-type modified!')
    }

