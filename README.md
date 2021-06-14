# aws-instance-stop

## Purpose
Deployed as Lambda function, script stops EC2 instances. Useful for all of those who forget to stop the instances and then complain about AWS 'being so expensive'. :)

## Usage
- Add to your EC2 instance(s) tag 'uptime' with appropriate value (in this example 'daytime').
- Deploy this script as Lambda
- Add a trigger 'EventBridge (CloudWatch Events)
- Create a new rule with appropriate Schedule expression.

