from ultralytics import YOLO
import os
import uuid

model = YOLO("model/best.pt")

def predict(image_path):
    results = model(image_path)

    output_path = os.path.join("static", f"result_{uuid.uuid4().hex}.jpg")
    results[0].save(filename=output_path)

    return output_path