from ultralytics import YOLO
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def predict(link):
    # Load a model
    model = YOLO("best2.pt")  # pretrained YOLOv8n model

    # Send a GET request to fetch the image
    try:
        response = requests.get(link)
    except:
        return "bruh"

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image from the response content
        try:
            image = Image.open(BytesIO(response.content))
        except:
            return "That's not even a picture"
        # Now `image` is a PIL Image object
    else:
        return "That's not even a picture"

    # Get results
    results = model(image, max_det=30, conf=0.01)

    # Look for max confidence
    # Todo: See how this works with videos
    max_con = 0
    conf = results[0].boxes.conf.cpu().numpy() #only do first result
    print(conf)
    max_con = conf[np.argmax(conf)]
    return f"This photo is {max_con * 100}% bridge"
