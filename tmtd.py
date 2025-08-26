from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image
import base64
import io
import os

app = Flask(__name__)

# Load the pre-trained model
# MODEL = load_model("model.h5")
MODEL = load_model("model_mnist_0.keras")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def recognize():
    try:
        # Get the image data from the request
        data = request.get_json()
        image_data = data['image']
        
        # Remove the data URL prefix
        image_data = image_data.split(',')[1]
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert PIL image to numpy array
        img_array = np.array(image)
        
        # Convert RGBA to RGB if necessary
        if img_array.shape[2] == 4:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
        
        # Convert to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        
        # Invert colors (canvas is white background with black drawing)
        # Model expects black background with white digit
        gray = cv2.bitwise_not(gray)
        
        # Resize to 28x28 pixels
        image_resize = cv2.resize(gray, (28, 28))
        
        # Normalize pixel values
        image_resize = image_resize / 255.0
        
        # Reshape for model input
        image_reshape = np.reshape(image_resize, [1, 28, 28])
        
        # Make prediction
        prediction = MODEL.predict(image_reshape)
        
        # Get predicted digit
        predicted_digit = int(np.argmax(prediction))
        
        return jsonify({"prediction": str(predicted_digit)})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to process image"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)
