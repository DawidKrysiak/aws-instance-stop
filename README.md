# aws-instance-stop

## Purpose
Deployed as Lambda function, script stops EC2 and RDS instances. Useful for all of those who forget to stop the instances and then complain about AWS 'being so expensive'. :)

## Usage
- Add to your EC2/RDS instance(s) tag 'uptime' with appropriate value (in this example 'daytime').
- Deploy this script as Lambda
- If you need the systems to stop/start automatically, create another lambda from the code, just change `stop_instances` and `stop_db_instances` to `start_instances` and `start_db_instances` respectivelly 
- Add a trigger(s) 'EventBridge (CloudWatch Events)' (e.g. start lambda triggered at 8AM, stop lambda at 8PM)
- Create a new rule with appropriate Schedule expression.
- create new role with policy: 

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "rds:StopDBInstance",
                "rds:DescribeDBInstances",
                "logs:CreateLogStream",
                "ec2:DescribeInstances",
                "ec2:StopInstances",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```
- attach it to Lambda as execution policy
