import matplotlib.pyplot as plt
import cv2
import numpy as np

def show_images(images, titles):
    """
    Display multiple images in a single row using Matplotlib.
    """
    n = len(images)
    plt.figure(figsize=(20, 5))  # Adjust the figure size for a single row
    for i in range(n):
        plt.subplot(1, n, i + 1)  # Set 1 row and 'n' columns
        plt.title(titles[i])
        if len(images[i].shape) == 2:  # Grayscale images
            plt.imshow(images[i], cmap="gray")
        else:  # Colored images
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.axis("off")  # Turn off axes for better visualization
    plt.tight_layout()
    plt.show()

def plot_edge_counts(images, titles):
    """
    Plot a bar chart comparing the edge pixel count for different preprocessed images.
    """
    counts = [cv2.countNonZero(cv2.Canny(img, 50, 150)) for img in images]
    plt.bar(titles, counts, color='skyblue')
    plt.xlabel('Images')
    plt.ylabel('Edge Pixel Count')
    plt.title('Comparison of Edge Detection Results')
    plt.show()

def plot_histogram_with_threshold(gray_image, return_threshold=False):
    """
    Compute and display a histogram of a grayscale image.
    Also compute an optimal threshold using Otsu's method and mark it on the histogram.
    
    Parameters:
      gray_image: a single-channel (grayscale) image (numpy array)
      return_threshold: If True, returns the computed threshold value.
    
    Returns:
      The computed threshold value if return_threshold is True; otherwise, None.
    """
    # Compute histogram of pixel intensities (0-255)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    
    # Compute the optimal threshold using Otsu's method
    ret, _ = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.plot(hist, color='blue')
    plt.title("Grayscale Histogram with Otsu's Threshold")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    
    # Mark the computed threshold value with a vertical dashed red line
    plt.axvline(x=ret, color='red', linestyle='--', label=f"Otsu Threshold: {ret:.2f}")
    plt.legend()
    plt.show()
    
    if return_threshold:
        return ret
