from preprocessing import to_grayscale, reduce_noise_gaussian, reduce_noise_median, reduce_noise_bilateral
from segmentation import detect_edges
from utils import show_images, plot_edge_counts
import cv2

image_path = "../images/image1.jpg"

try:
    
    image = cv2.imread(image_path)

    
    if image is None:
        print("Error: Image not found or unable to load.")
        exit()

    grayscale_image = to_grayscale(image)  
    gaussian_blur = reduce_noise_gaussian(grayscale_image)  
    median_blur = reduce_noise_median(grayscale_image)  
    bilateral_filter = reduce_noise_bilateral(grayscale_image)  

    edges = detect_edges(grayscale_image, lower_threshold=50, upper_threshold=150)  

    titles = [
        "Original Image",
        "Grayscale Image",
        "Gaussian Blur",
        "Median Blur",
        "Bilateral Filtering",
        "Edge Detection"
    ]
    images = [image, grayscale_image, gaussian_blur, median_blur, bilateral_filter, edges]

    show_images(images, titles)

    plot_edge_counts(
        [grayscale_image, gaussian_blur, median_blur, bilateral_filter],
        ["Grayscale", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
    )

except Exception as e:
    print(f"An error occurred: {e}")
