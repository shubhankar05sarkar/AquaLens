import cv2

def detect_edges(image, lower_threshold=50, upper_threshold=150):
    
    return cv2.Canny(image, lower_threshold, upper_threshold)
