import boto3
import json
import datetime
import pymysql as mariadb

rds_id = 'rds-db'
db_name = 'rdsMariaDev'
username_name = 'masteruser'
user_password = 'masterpassword'
rds_endpoint = ''

rds_client = boto3.client('rds')
response = rds_client.describe_db_instances(
    DBInstanceIdentifier=rds_id)

rds_endpoint = json.dumps(response, response['DBInstance'][0]['Endpoint']['Address'])
print(rds_endpoint)