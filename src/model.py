import cv2
from ultralytics import YOLO


MODEL_PATH = r"C:\Users\shubh\OneDrive\Desktop\Projects\AquaLens\models\best.pt"

model = YOLO(MODEL_PATH)

def predict(image):
    
    results = model.predict(source=image, imgsz=640, verbose=False)
    return results

def detect_and_draw(image):
    
    results = model.predict(source=image, imgsz=640, verbose=False)
    
    plot_img = results[0].plot()
    return plot_img 
