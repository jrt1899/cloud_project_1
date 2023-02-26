import boto3

sqs = boto3.resource('sqs',region_name='us-east-1')
req_queue = sqs.get_queue_by_name(QueueName='RequestQueue')

for message in queue.receive_messages(MessageAttributeNames=['filename']):
    file_name = ''
    if message.message_attributes is not None:
        file_name = message.message_attributes.get('filename').get('StringValue')
        image = bytes(message.body,'utf-8')

        #create image
        message.delete()
        f = open('output_folder/'+file_name,'wb')
        f.write(data)
        f.close()

        
            
