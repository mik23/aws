import boto3
import json

sg_name = 'rds-sg-dev-demo'
sg_description = 'Rds Security Group'
my_ip_cidr = '0.0.0.0/0' #Public access to the DB using username and password

# EC2 client to create the security group
ec2_client = boto3.client('ec2')

#Security Group
response = ec2_client.create_security_group(
    Description=sg_description,
    GroupName=sg_name)
print(json.dumps(response, indent=2, sort_keys=True))

# Add Rule for the security group
response = ec2_client.authorize_security_group_ingress(
    CidrIp=my_ip_cidr,
    FromPort=3306,
    ToPort=3306,
    GroupName=sg_name,
    IpProtocol='tcp'
)

print("Security Group  created!", response)