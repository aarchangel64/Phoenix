from google.cloud import vision
from google.cloud.vision import types


def fire_vision(input_image):
    client = vision.ImageAnnotatorClient()

    #TODO: figure out what format we are recieving image data in and covert it to this
    image = types.Image(content=input_image)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
		if (label.description == fire)
			moveForward()

