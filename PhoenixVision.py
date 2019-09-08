# example parameter - "python 2 PhoenixVision.py fire.png"

from __future__ import print_function

import json
import os
import requests as r
from base64 import b64encode


def read_google_api_key():
    key = 'AIzaSyCttWReHK373rf_kOr2BTWuQCyhiRHunfY'


def make_image_data_list(images, b64=True):

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
    if not b64:
        for img in images:
            with open(img, 'rb') as f:
                ctxt = b64encode(f.read()).decode()
                img_requests.append(content(ctxt))
    else:
        for img in images:
            img_requests.append(content(img))
    return img_requests


def make_image_data(images, b64=True):
    img_dict = make_image_data_list(images, b64)
    return json.dumps({"requests": img_dict}).encode()


def request_vision_api(image, b64=True):
    api_key = read_google_api_key()
    response = r.post('https://vision.googleapis.com/v1/images:annotate',
                      data=make_image_data([image], b64),
                      params={'key': 'AIzaSyCttWReHK373rf_kOr2BTWuQCyhiRHunfY'},
                      headers={'Content-Type': 'application/json'})
    return response

if __name__ == '__main__':
    import sys

    arguments = sys.argv

    resp = request_vision_api(arguments[1], b64=False)
    dict_google_response = json.loads(resp.content)
    str_to_write = json.dumps(dict_google_response, indent=4)
    print(str_to_write)

    try:
        for c in dict_google_response['responses'][0]['labelAnnotations']:
            if c['description'] == "Fire" or c['description'] == "Heat" or c['description'] == "Flame":
                print("fire detected") 
                #moveForward() 
                break
    except json.decoder.JSONDecodeError:
        print("Fire not detected")
