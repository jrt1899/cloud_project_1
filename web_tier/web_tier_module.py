import boto3

sqs = boto3.resource('sqs',region_name='us-east-1')

#configurations request queue 
req_queue = queue = sqs.get_queue_by_name(QueueName='RequestQueue')

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