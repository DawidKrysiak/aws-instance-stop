import boto3
import os

def lambda_handler(event, context):

    region = os.environ['AWS_REGION']
    ec2 = boto3.client('ec2', region_name=region)
    rds = boto3.client('rds',region_name=region)

    reservations = ec2.describe_instances().get('Reservations', [])
    instances = []
    for r in reservations:
        for i in r['Instances']:
            instances.append(i)

    for instance in instances:
        print("Found instance: ",instance['InstanceId']," in status: ",instance['State']['Name'])
        try:
            for tag in instance['Tags']:
                if tag['Key'] == 'uptime':
                    if tag['Value'] == 'daytime':
                        instance = instance['InstanceId']
                        response = ec2.stop_instances(InstanceIds=[instance])
                        print("stopping instance", instance)
        except:
            print("no instances")

    database_instances = rds.describe_db_instances().get('DBInstances', [])

    for database in database_instances:
        db = database['DBInstanceIdentifier']
        if database['DBInstanceStatus'] == 'running':
            print('db is running :',db)
            for tag in database['TagList']:
                if tag['Key'] == 'uptime':
                    uptime = tag['Value']
                    if uptime == 'daytime':
                        response = rds.stop_db_instance(DBInstanceIdentifier=db)
        else:
            print(db, 'is not running at this time')
