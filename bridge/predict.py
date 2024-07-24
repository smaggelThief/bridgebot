from ultralytics import YOLO

# Load a model
model = YOLO("best.pt")  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model(["im1.jpg"], conf=0.1)  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result2.jpg")  # save to disk