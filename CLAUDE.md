# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"Tell me the digit" (tmtd) - A Flask web application for handwritten digit recognition using a pre-trained Keras model. Users can draw a digit on a canvas, and the application will predict which digit (0-9) was drawn using machine learning.

## Key Files

- `tmtd.py` - Main Flask application with digit recognition endpoint
- `model_mnist_0.keras` - Pre-trained Keras model for MNIST digit recognition
- `templates/index.html` - Drawing canvas interface
- `templates/layout.html` - Base HTML template
- `requirements.txt` - Python dependencies
- `heroku.yml` - Heroku container deployment manifest
- `Dockerfile` - Container configuration for Heroku deployment
- `Procfile` - Legacy file (not used due to slug size constraints)

## Development Commands

### Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
. .venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### Run Application

```bash
# Development mode with Flask
flask --app tmtd run --port=5001 --host=0.0.0.0 --debug

# Production mode with Gunicorn
gunicorn tmtd:app
```

## Architecture

Flask application that:
- Serves a drawing canvas interface at `/` (GET)
- Processes digit images at `/` (POST) endpoint
- Accepts base64-encoded canvas images via JSON
- Preprocesses images (grayscale conversion, resizing to 28x28, normalization)
- Uses TensorFlow/Keras model for prediction
- Returns predicted digit as JSON response

### Image Processing Pipeline
1. Decode base64 image from canvas
2. Convert RGBA to RGB if necessary
3. Convert to grayscale
4. Invert colors (canvas uses white background, model expects black)
5. Resize to 28x28 pixels
6. Normalize pixel values (0-1 range)
7. Reshape for model input
8. Predict using trained model

## Dependencies

- Flask 3.0.3 - Web framework
- TensorFlow 2.20.0 - Machine learning framework
- OpenCV (cv2) - Image processing
- NumPy 1.26.2 - Numerical operations
- Pillow 10.3.0 - Image handling
- Gunicorn 21.2.0 - Production WSGI server

## Deployment

### Heroku (Container Stack)
- Uses containerized deployment with `heroku.yml` manifest
- Docker-based deployment to avoid slug size limitations
- `Dockerfile` builds Python 3.11 slim image with all dependencies
- Gunicorn serves the application on Heroku's dynamic PORT
- Note: `Procfile` exists but is not used (slug-based deployment fails due to large TensorFlow dependencies)

## Development Notes

- Python 3 virtual environment recommended
- Default port 5001 (avoids conflicts with common port 5000)
- Model expects 28x28 grayscale images with black background
- Canvas drawings are inverted to match model expectations
- Error handling for image processing failures