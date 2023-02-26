import app_tier_1 as ap
import image_classification as ic

if __name__ == '__main__':
     while True :
        filename = ap.get_response()

        if(filename == '-1') :
            continue

        class_name = ic.classify_image(filename)
        #print(class_name,filename)
        s3BucketMsg = ap.add_image_to_s3(filename, class_name)
        resSqsMsg = ap.send_response(filename, class_name)
	    # delete_file_from_upload_folder()
