from google.cloud import vision
from google.cloud.vision import types
import cv2


def fire_vision(input_image):

	client = vision.ImageAnnotatorClient().from_service_account_json('res/account.json')
	image = client.image(content=cv2.imencode('.jpg', input_image)[1].tostring())

	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('Labels:')
	for label in labels:
		print(label.description)
		if (label.description == fire):
			print("test")
