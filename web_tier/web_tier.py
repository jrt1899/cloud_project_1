from flask import Flask, redirect, url_for, request
import os, time, sys
import base64
import web_tier_module as wt

# import app_tier_main as app

#initializations
app = Flask(__name__)

# Run python3 web_tier.py in one terminal
# Run curl -X POST -F myfile=@test_18.JPEG 'http://localhost:5000/accept_images' in another terminal
files = []
@app.route('/accept_images',methods=['POST'])
def accept_images():

    file = request.files['myfile']

    file.save(os.path.join(os.getcwd(),'upload_folder', file.filename))
    converted_string = ''
    with open(os.path.join(os.getcwd(),'upload_folder', file.filename), "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())

    print('incoming request for image : ',file.filename)

    #send sqs message
    req = wt.send_message(file.filename,converted_string.decode('utf-8'))
    files.append(file.filename)
    # time.sleep(10)
    # app_tier_main.callAppTier()

    #receive sqs message
    # time.sleep(3)

    while True:
        res = wt.receive_message(file.filename)
        if res != '-1':
            break
    print('sending response : ',res)

    #remove file from upload folder
    if os.path.exists(os.path.join(os.getcwd(),'upload_folder', file.filename)):
        os.remove(os.path.join(os.getcwd(),'upload_folder', file.filename))

    return res

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(host = "0.0.0.0", port = 5000, debug = True)