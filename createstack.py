import boto3
import re  
import datetime
import logging
ec2 = boto3.resource('ec2')
ec = boto3.client('ec2', region_name='us-east-1')  
iam = boto3.client('iam')
def lambda_handler(event, context):
    client = boto3.client('cloudformation')
    response = client.create_stack(
        StackName='your-cloud-stack',
        TemplateURL='https://s3.amazonaws.com/your-bucket-url.yml',
        Parameters=[
            {'ParameterKey': 'ClusterType', 'ParameterValue': 'name'},
            {'ParameterKey': 'Environment', 'ParameterValue': 'dev'},
            {'ParameterKey': 'RunType', 'ParameterValue': 'None'},
            {'ParameterKey': 'EMRClusterName', 'ParameterValue': 'resource-name'},
            {'ParameterKey': 'NumberOfCoreInstances', 'ParameterValue': '10'},
            {'ParameterKey': 'MasterInstanceType', 'ParameterValue': 'i3.8xlarge'},
            {'ParameterKey': 'CoreInstanceType', 'ParameterValue': 'i3.8xlarge'},
            {'ParameterKey': 'HiveMetaStore', 'ParameterValue': 'jdbc:mysql://your-data-base-name createDatabaseIfNotExist=true'},
            {'ParameterKey': 'HiveMetaStorePassword', 'ParameterValue': 'your-password'},
            {'ParameterKey': 'DynamoDBTable', 'ParameterValue': 'your-table'},
            {'ParameterKey': 'HostedZoneName', 'ParameterValue': 'your-hosted-zone.local'},
            {'ParameterKey': 'CNAME', 'ParameterValue': 'your-cname-and-value.local'},
        ]
    )
    
    return(response)
