# model.py
import cv2
from ultralytics import YOLO

# Update the MODEL_PATH to point to your model file.
# For example, if you placed your model file in a folder named "models" at the project root:
MODEL_PATH = r"C:\Users\shubh\OneDrive\Desktop\Projects\AquaLens\models\best.pt"

# Load the YOLO model using ultralytics
model = YOLO(MODEL_PATH)

def predict(image):
    """
    Run YOLO inference on the provided image (BGR format) and return the raw results.
    """
    results = model.predict(source=image, imgsz=640, verbose=False)
    return results

def detect_and_draw(image):
    """
    Runs YOLO inference on the given image and returns an image with bounding boxes drawn.
    The input image should be in BGR format.
    """
    results = model.predict(source=image, imgsz=640, verbose=False)
    # Use the built-in plot method of the first result to draw bounding boxes
    plot_img = results[0].plot()
    return plot_img  # plot_img is in BGR format
