# CSE546 - Cloud Computing - Project 1

### Created By:  
Dhyey Pandya  
Jaykumar Rajeshbhai Tandel  
Sumedh Shridhar Joshi  

## Member Tasks
### Dhyey Pandya:  
	I have been responsible for designing a part of the App Tier, which  involved the classification of the images received from AWS SQS  RequestQueue, followed by uploading the images to AWS S3 bucket called  ‘cloud-project-1-input-images’ and the text files containing the image  name and its top-1 classification result to the bucket called  ‘cloud-project-1-output-image-class’. I have also developed the App Tier  part to send the obtained classification result to the AWS SQS  ResponseQueue. I have also been involved with setting up the AWS SQS  Queues, S3 buckets and final testing of the entire application.  
### Jaykumar Rajeshbhai Tandel:  
	I designed the Flask web-app on an EC2 instance. I am responsible for  its functionalities consisting of accepting parallel requests coming  from the client, sending input images to the RequestQueue, accepting  responses coming from the ResponseQueue and sending correct responses to  the client.   
### Sumedh Shridhar Joshi:  
	I have been involved with designing the app-tier Amazon Machine Image  (AMI), setting up the Cloudwatch Scale-in and Scale-out alarms, and the  EC2 AutoScaling Group that would be in accordance with the Cloudwatch  alarms to add and remove the instances. I have been involved with  testing of the entire application and monitoring the status of the  alarms and AutoScale Instances.  

## Execution Steps and Services Details:
### AWS Account Credntials:


### Web Tier:
    Web Tier Name: web_tier
    Web Tier URL: [Here](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#InstanceDetails:instanceId=i-0510942fdb2be6d6f)  
    Web Tier URL Once the Instance is Running: {web-tier-ip-address}

### SQS:
    Request Queue Name: RequestQueue  
    Response Queue Name: ResponseQueue

### S3:
    Input Images Bucket: cloud-project-1-input-images
    Output Image/Classname Bucket: cloud-project-1-output-image-class

### Cloudwatch Alarms:
    Scale In Alarm Name: Scale in  
    Scale Out Alarm Name: Scale out
