import boto3
import base64
import os

sqs = boto3.client('sqs',region_name='us-east-1')
req_queue_url = 'https://sqs.us-east-1.amazonaws.com/749917607921/RequestQueue'
res_queue_url = 'https://sqs.us-east-1.amazonaws.com/749917607921/ResponseQueue'

def get_response() :

    response = sqs.receive_message(
        QueueUrl=req_queue_url,
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
    if('Messages' not in response) :
        return '-1'

    message = response['Messages'][0]

    filename = message['MessageAttributes']['filename']['StringValue']
    receipt_handle = message['ReceiptHandle']


    message_body = bytes(message['Body'],encoding='utf-8')

    decodeit = open(os.path.join(os.getcwd(),'upload_folder', filename), 'wb')
    decodeit.write(base64.b64decode((message_body)))
    decodeit.close()
    print(filename)

    sqs.delete_message(
        QueueUrl=req_queue_url,
        ReceiptHandle=receipt_handle
    )

    return filename#filename
    #delete message
    #add image to s3
    #classify



def add_image_to_s3(filename, class_name):
    try:
        s3 = boto3.client('s3',region_name='us-east-1')
        image = os.path.join(os.getcwd(),'upload_folder', filename)
        s3.upload_file(image,'project-1-input-images', filename)
        with open(image, 'rb') as data:
            result = filename[:-5]
            s3.upload_fileobj(data, 'project-2-output-image-class', result, ExtraArgs={'Metadata': {result: class_name}})
    except Exception as e:
        print('Error Occurred while Updating S3 Buckets!')
        return e
    
    return 'S3 Buckets Updated!'

def send_response(filename, class_name):
    try:
        response = sqs.send_message(
            QueueUrl = res_queue_url,
            DelaySeconds = 10,
            MessageAttributes={
                'filename': {
                    'DataType': 'String',
                    'StringValue': filename
                }
            },
            MessageBody=(class_name)
        )
    except Exception as e:
        print('Error Occurred while Sending Message to Response Queue!')
        return e
    
    return 'Response Sent!'


