import boto3

sqs = boto3.client('sqs', region_name='us-east-1')

queue = sqs.create_queue(QueueName='SQS_IDP_ADAPTER_QUEUE',
                         Attributes={
                             'DelaySeconds': '60',
                             'MessageRetentionPeriod': '86400'
                         })

print('Queue URL: ', queue['QueueUrl'])
