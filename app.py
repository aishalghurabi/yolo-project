from flask import Flask, request, jsonify
import os
from model import predict

app = Flask(__name__)

@app.route("/")
def index():
    return "YOLO API is running"

@app.route("/predict", methods=["POST"])
def run_prediction():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]

    filepath = os.path.join("input.jpg")
    file.save(filepath)

    output_path = predict(filepath)