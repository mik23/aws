import boto3
import json

sg_name = 'rds-sg-dev-demo'
rds_id = 'rds-db'
db_name = 'rdsMariaDev'

username_name = 'masteruser'
user_password = 'masterpassword'
admin_email = 'marcotrigiano.m@gmail.com'
sg_id_number = ''
rds_enpoint = ''

# retrieve security group id number to use credentials of the rds instance
ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ])
sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"', '')

# RDS client
rds_client = boto3.client('rds')

response = rds_client.create_db_instance(
    DBInstanceIdentifier=rds_id,
    DBName=db_name,
    DBInstanceClass='db.t2.micro',
    Engine='mariadb',
    MasterUsername=username_name,
    MasterUserPassword=user_password,
    VpcSecurityGroupIds=[sg_id_number],
    AllocatedStorage=20,
    Tags=[{
        'Key': 'POC-PetProject-Email',
        'Value': admin_email
    }]
)

print('Creating the RDS instance...')
waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_id)

print('Done!')