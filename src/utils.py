import matplotlib.pyplot as plt
import cv2
import numpy as np

def show_images(images, titles):
   
    n = len(images)
    plt.figure(figsize=(20, 5))  
    for i in range(n):
        plt.subplot(1, n, i + 1)  
        plt.title(titles[i])
        if len(images[i].shape) == 2:  
            plt.imshow(images[i], cmap="gray")
        else:  
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.axis("off")  
    plt.tight_layout()
    plt.show()

def plot_edge_counts(images, titles):
    
    counts = [cv2.countNonZero(cv2.Canny(img, 50, 150)) for img in images]
    plt.bar(titles, counts, color='skyblue')
    plt.xlabel('Images')
    plt.ylabel('Edge Pixel Count')
    plt.title('Comparison of Edge Detection Results')
    plt.show()

def plot_histogram_with_threshold(gray_image, return_threshold=False):
    
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    
    
    ret, _ = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    
    plt.figure(figsize=(8, 6))
    plt.plot(hist, color='blue')
    plt.title("Grayscale Histogram with Otsu's Threshold")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    
    
    plt.axvline(x=ret, color='red', linestyle='--', label=f"Otsu Threshold: {ret:.2f}")
    plt.legend()
    plt.show()
    
    if return_threshold:
        return ret
