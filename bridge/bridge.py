from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco8/data.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
path = model.export(format="torchscript")  # export the model to ONNX format