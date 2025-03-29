from preprocessing import to_grayscale, reduce_noise_gaussian, reduce_noise_median, reduce_noise_bilateral
from segmentation import detect_edges
from utils import show_images, plot_edge_counts
import cv2

# Path to the image
image_path = "../images/image1.jpg"
#image_path = "../images/image2.jpeg"
#image_path = "../images/image3.jpeg"

try:
    # Load the original image using OpenCV
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Image not found or unable to load.")
        exit()

    # Preprocessing steps
    grayscale_image = to_grayscale(image)  # Convert to grayscale
    gaussian_blur = reduce_noise_gaussian(grayscale_image)  # Apply Gaussian Blur
    median_blur = reduce_noise_median(grayscale_image)  # Apply Median Blur
    bilateral_filter = reduce_noise_bilateral(grayscale_image)  # Apply Bilateral Filter

    # Edge Detection
    edges = detect_edges(grayscale_image, lower_threshold=50, upper_threshold=150)  # Grayscale Edges

    # Titles and images to display
    titles = [
        "Original Image",
        "Grayscale Image",
        "Gaussian Blur",
        "Median Blur",
        "Bilateral Filtering",
        "Edge Detection"
    ]
    images = [image, grayscale_image, gaussian_blur, median_blur, bilateral_filter, edges]

    # Display all images
    show_images(images, titles)

    # Plot edge pixel counts for the grayscale edge detection result
    plot_edge_counts(
        [grayscale_image, gaussian_blur, median_blur, bilateral_filter],
        ["Grayscale", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
    )

except Exception as e:
    print(f"An error occurred: {e}")
