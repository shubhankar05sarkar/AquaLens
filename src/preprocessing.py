import cv2

def to_grayscale(image):
    """Convert a BGR image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def reduce_noise_gaussian(image, kernel_size=(7, 7)):
    """Apply Gaussian Blur to reduce noise."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def reduce_noise_median(image, kernel_size=7):
    """Apply Median Blur to reduce salt-and-pepper noise."""
    return cv2.medianBlur(image, kernel_size)

def reduce_noise_bilateral(image, diameter=15, sigma_color=100, sigma_space=100):
    """Apply Bilateral Filtering to reduce noise while preserving edges."""
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
