import boto3
import base64
import os

sqs = boto3.client('sqs',region_name='us-east-1')
req_queue_url = 'https://sqs.us-east-1.amazonaws.com/104949213169/RequestQueue'
res_queue_url = 'https://sqs.us-east-1.amazonaws.com/104949213169/ResponseQueue'

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

    # decodeit = open(os.path.join(os.getcwd(),'upload_folder', filename), 'wb')
    decodeit = open(os.path.join('/home/ubuntu/app_tier/upload_folder', filename), 'wb')
    decodeit.write(base64.b64decode((message_body)))
    decodeit.close()
    #print(filename)

    sqs.delete_message(
        QueueUrl=req_queue_url,
        ReceiptHandle=receipt_handle
    )

    return filename#filename



def add_image_to_s3(filename, class_name):
    #print('called fn', filename)
    s3 = boto3.client('s3',region_name='us-east-1')
    image = os.path.join('/home/ubuntu/app_tier/upload_folder', filename)
    # image = os.path.join(os.getcwd(),'upload_folder', filename)
    s3.upload_file(image,'cloud-project-1-input-images', filename)
    txtfile = filename[:-5]
    #print(txtfile)
    with open(os.path.join('/home/ubuntu/app_tier/output_folder', txtfile), 'wt') as tmpFile:
        tmpFile.write(str(class_name))
        #print(class_name)
    s3.upload_file(os.path.join('/home/ubuntu/app_tier/output_folder', txtfile), 'cloud-project-1-output-image-class', txtfile)
    if os.path.exists(os.path.join('/home/ubuntu/app_tier/output_folder', txtfile)):
        os.remove(os.path.join('/home/ubuntu/app_tier/output_folder', txtfile))
    return 'S3 Buckets Updated!'

def send_response(filename, class_name):
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
    return 'Response Sent!'


