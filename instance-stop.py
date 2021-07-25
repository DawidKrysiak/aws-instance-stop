import boto3
import os

def lambda_handler(event, context):

    region = os.environ['AWS_REGION']
    ec2 = boto3.client('ec2', region_name=region)

    reservations = ec2.describe_instances().get('Reservations', [])
    instances = []
    for r in reservations:
        for i in r['Instances']:
            instances.append(i)

    for instance in instances:
        try:
            for tag in instance['Tags']:
                if tag['Key'] == 'uptime':
                    if tag['Value'] == 'daytime':
                        instance = instance['InstanceId']
                        response = ec2.stop_instances(InstanceIds=[instance])
                        print("stopping instance", instance)
        except:
            print("no instances")
