# Cat vs Dog Classifier with TensorFlow Keras and Flask

This project provides a Convolutional Neural Network (CNN) model built using TensorFlow Keras to classify images as either a cat or a dog. The trained model is hosted using a Flask web application, allowing users to upload an image, run it through the model, and receive a classification result.

## Features

- **CNN Architecture**: The model uses a CNN architecture to classify images.
- **Flask Web Application**: A simple Flask web application to host the model and provide a user interface for image classification.
- **Base64 Image Handling**: The web app accepts an image, converts it to base64, and decodes it in the backend for inference.
- **Google Cloud Platform (GCP) Deployment**: The code is structured to be easily deployable on GCP.

## Requirements

- Python 3.x
- TensorFlow
- Flask
- NumPy
- PIL (Pillow)
- Base64

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cat-vs-dog-classifier.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cvd
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open a web browser and go to http://localhost:5000.
3. Upload an image using the provided interface.
4. Click the 'Classify' button to run the image through the model.
5. View the classification result on the web page.
