import cv2

def to_grayscale(image):
    
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def reduce_noise_gaussian(image, kernel_size=(7, 7)):
    
    return cv2.GaussianBlur(image, kernel_size, 0)

def reduce_noise_median(image, kernel_size=7):
    
    return cv2.medianBlur(image, kernel_size)

def reduce_noise_bilateral(image, diameter=15, sigma_color=100, sigma_space=100):
    
    return cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
