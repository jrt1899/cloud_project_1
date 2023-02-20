import app_tier_1 as ap

if __name__ == '__main__':
	while True :

		filename = ap.get_response()

		if(filename == '-1'):
			break

		class_name = classify_image()
		ap.add_image_to_s3(filename,class_name)
		send_response()
		delete_file_from_upload_folder()
