import os
from ultralytics import YOLO
import sys
import urllib.request
from urllib.request import Request, urlopen

# Load a model
model = YOLO("best.pt")  # pretrained YOLOv8n model

# Run batched inference on a list of images
# results = model(source="im2.jpg", imgsz=800, conf=0.01, max_det=40)  # return a list of Results objects
link = sys.argv[1]
req = Request(
    url=link, 
    headers={'User-Agent': 'Mozilla/5.0'}
)
resource = urlopen(req)
output = open("im1.jpg","wb")
output.write(resource.read())
output.close()


model.predict("im1.jpg", max_det=30, conf=0.01, save_conf=True, save_txt=True, stream=False)

f = open("runs/detect/predict/labels/im1.txt", "r")
max_con = 0
for x in f:
    data = x.split()
    if float(data[5]) > max_con:
        max_con = float(data[5])
print("This photo is ", (max_con * 100),"%", " bridge")

f.close()
os.remove("im1.jpg")
os.remove("runs/detect/predict/labels/im1.txt")
os.rmdir("runs/detect/predict/labels")
os.rmdir("runs/detect/predict")
# Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     obb = result.obb  # Oriented boxes object for OBB outputs
#     result.show()  # display to screen
#     result.save(filename="result.jpg")  # save to disk