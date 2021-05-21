### AWS Exercises
#### RDS DB

After configuring the your account with ```aws configure```

Make sure a default vpc is available in your account and create at least couple of default subnets in multiAZ 
```
aws ec2 create-default-subnet --availability-zone us-east-1a
aws ec2 create-default-subnet --availability-zone us-east-1b
```
 
1. Create the security Group ```securityGroup.py```
2. Spin a MariaDB instance up ```spingUpRDS.py```