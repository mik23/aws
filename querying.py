import boto3
import json
import datetime
import pymysql as mariadb

rds_id = 'rds-db'
db_name = 'rdsMariaDev'
user_name = 'masteruser'
user_password = 'masterpassword'
rds_endpoint = ''

rds_client = boto3.client('rds')
response = rds_client.describe_db_instances(DBInstanceIdentifier=rds_id)

rds_endpoint = json.dumps(response['DBInstances'][0]['Endpoint']['Address'])
rds_endpoint = rds_endpoint.replace('"', '')

db_connection = mariadb.connect(host=rds_endpoint,
 user=user_name,
 password=user_password, 
 database=db_name)

cursor = db_connection.cursor()

try:
    cursor.execute("CREATE TABLE ADS( ads_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, description VARCHAR(100))")
    print("table created!")
    
sql = "INSERT INTO `ADS` (`description`) VALUES (%s)"
cursor.execute(sql, ('ads about things'))
cursor.execute(sql, ('ads about stuff'))
db_connection.commit()
    print('Iserted Data to Database!')
except mariadb.Error as e:
    print("Error: {}".format(e))
finally:
    db_connection.close()
