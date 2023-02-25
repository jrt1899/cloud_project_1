import boto3

sqs = boto3.resource('sqs',region_name='us-east-1')

#configurations request queue 
req_queue = queue = sqs.get_queue_by_name(QueueName='RequestQueue')

sqsClient = boto3.client('sqs',region_name='us-east-1')
res_queue = queue = sqs.get_queue_by_name(QueueName='ResponseQueue')
res_queue_url = 'https://sqs.us-east-1.amazonaws.com/749917607921/ResponseQueue'

#configurations response queue

def send_message(file_name,content) :
	print(file_name)
	print(req_queue.url)
	response = req_queue.send_message(
	    QueueUrl=req_queue.url,
	    DelaySeconds=10,
	    MessageAttributes={
	        'filename': {
	            'DataType': 'String',
	            'StringValue': file_name
	        }
	    },
    	MessageBody=(content)
	)

	return 'Sent'


def receive_message():
	print(res_queue.url)
	response = sqsClient.receive_message(
		QueueUrl=res_queue.url,
		AttributeNames=[
			'filename'
		],
		MaxNumberOfMessages=1,
		MessageAttributeNames=[
			'All'
		],
		VisibilityTimeout=0,
		WaitTimeSeconds=0
    )
	
	if('Messages' not in response):
		return '-1'

	message = response['Messages'][0]

	filename = message['MessageAttributes']['filename']['StringValue']
	receipt_handle = message['ReceiptHandle']


	# message_body = (message['classname'])
	message_body = message['Body']

	print(message_body)
    
	deletedRes = sqsClient.delete_message(
        QueueUrl=res_queue_url,
        ReceiptHandle=receipt_handle
    )

	return message_body
