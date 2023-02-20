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



def add_image_to_s3(filename) :
    s3 = boto3.client('s3',region_name='us-east-1')
    image = s3.upload_file(os.path.join(os.getcwd(),'upload_folder', filename),'project-1-input-images', filename)
    #result = s3.uplode_file(r'PATH','project-2-output-image-class', 'FILENAME')




