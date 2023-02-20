from flask import Flask, redirect, url_for, request
import os
import base64
import web_tier_module as wt


#initializations
app = Flask(__name__)

# Run python3 web_tier.py in one terminal
# Run curl -X POST -F myfile=@test_18.JPEG 'http://localhost:5000/accept_images' in another terminal

@app.route('/accept_images',methods=['POST'])
def accept_images():
    
    file = request.files['myfile']

    file.save(os.path.join(os.getcwd(),'upload_folder', file.filename))
    converted_string = ''
    with open(os.path.join(os.getcwd(),'upload_folder', file.filename), "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    print(type(converted_string.decode('utf-8')))
    #delete file from upload folder


    #send sqs message
    res = wt.send_message(file.filename,converted_string.decode('utf-8'))

    return '1'
    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
