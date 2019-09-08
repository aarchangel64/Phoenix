# example parameter - "python 2 PhoenixVision.py fire.png"

import json
import os
import requests as r
from base64 import b64encode
import sys


def detect_image(image):
	resp = request_vision_api(image)
	dict_google_response = json.loads(resp.content)
	str_to_write = json.dumps(dict_google_response, indent=4)
	print(str_to_write)

	try:
		for c in dict_google_response['responses'][0]['labelAnnotations']:
			if c['description'] == "Fire" or c['description'] == "Heat" or c['description'] == "Flame":
				print("fire detected")
				# moveForward()
				break
	except json.decoder.JSONDecodeError:
		print("Fire not detected")


def request_vision_api(image):
	api_key = read_google_api_key()
	response = r.post('https://vision.googleapis.com/v1/images:annotate',
	                  data=make_image_data([image]),
	                  params={'key': 'AIzaSyCttWReHK373rf_kOr2BTWuQCyhiRHunfY'},
	                  headers={'Content-Type': 'application/json'})
	return response


def make_image_data(images):
	img_dict = make_image_data_list(images)
	return json.dumps({"requests": img_dict}).encode()


def make_image_data_list(images):
	def content(context):
		return {
			'image': {'content': context},
			'features': [
				{
					'type': 'LABEL_DETECTION',
					'maxResults': 10
				}
			]
		}

	img_requests = []
	for img in images:
		img_requests.append(content(img))
	return img_requests


def read_google_api_key():
	key = 'AIzaSyCttWReHK373rf_kOr2BTWuQCyhiRHunfY'
