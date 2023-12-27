# AWS-Optimization

## Project Description
In real-world cloud solutions, organizations have to take care of the AWS environment and make sure it complies with the organizational policies while maintaining the regulations of assigning "Least Privilege". We aim to achieve the same while making efficient AWS usage with this project.

## Resources
The resources and technologies used in the project are:
  - AWS Lambda
  - AWS Cloudwatch
  - AWS EC2
  - AWS EBS
  - Python

## Project Workflow
In this continuously evolving project, we are going to employ AWS resources to automate the checks and actions one has to take to optimize and make AWS usage efficient. Our use cases are:

* ## Monitor and respond to newly created EBS volumes that are of type GP2 and convert them to type GP3:
  - A Lambda function to be triggered when an Amazon Elastic Block Store (EBS) volume is created.
  - AWS Cloudwatch is used to trigger the function and also to collect log streams for efficient troubleshooting.
  - The "lambda_handler" script is written in Python 3, employs [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), and is available for perusal and feedback.
 
* ## Identifying Stale Resources and deleting them according to organization-specific guidelines:
  - We are using stale EBS snapshots as a starting point.
  - A Lambda function is to be triggered at a particular time interval (for example, once every week) using Cloudwatch events.
  - The Lambda function fetches all EBS snapshots owned by the same account ('self') and also retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks if the associated volume (if exists) is not associated with any active instance. If it finds a stale snapshot, it deletes it, effectively optimizing storage costs.
  - The "lambda_handler" script is written in Python 3, employs [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), and is available for perusal and feedback.
