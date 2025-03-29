# **AquaLens**

AquaLens is an innovative image processing application designed to enhance underwater images for better analysis. It uses advanced preprocessing techniques to assist in marine monitoring and conservation efforts. The project includes interactive tools to visualize histograms, detect edges, and predict threshold values for efficient image analysis.

---

## **Features**
- **Image Preprocessing:**
  - Convert images to grayscale.
  - Noise reduction using Gaussian, Median, and Bilateral filters.
- **Edge Detection:**
  - Detect and highlight edges using Canny edge detection.
- **Threshold Analysis:**
  - Calculate optimal threshold values using Otsu's method.
  - Visualize histograms with thresholds marked.
- **Interactive GUI:**
  - User-friendly interface for image selection, processing, and visualization.

---

## **Technologies Used**
- **Languages:** Python
- **Libraries:** OpenCV, NumPy, Matplotlib, Tkinter

---

## **Usage**
### **1. Launch the GUI**
   - Start the GUI using the command `python gui.py`.
   - Browse and select an underwater image for processing.

### **2. Preprocessing Options**
   - Apply grayscale conversion and noise reduction filters.

### **3. Analyze Results**
   - View histograms and calculate threshold values.
   - Detect edges and visualize the output.

---

Here's the updated **Screenshots** section in the `README.md` file with placeholders for the images you've specified:

---

Here's the updated **Screenshots** section, now including a comparison of edge detection techniques:

---

## **Screenshots**

### **1. AquaLens GUI**  
![AquaLens GUI](screenshots/AquaLens_GUI.png)  
*This is the main interface of AquaLens where users can upload and process underwater images.*

---

### **2. Grayscale Conversion Results**  
![Grayscale Conversion Results](screenshots/Grayscale_Conversion.png)  
*The result of converting an underwater image to grayscale for further processing.*

---

### **3. Gaussian Blur Results**  
![Gaussian Blur Results](screenshots/Gaussian_Blur.png)  
*Noise reduction using Gaussian Blur to enhance image clarity.*

---

### **4. Median Blur Results**  
![Median Blur Results](screenshots/Median_Blur.png)  
*Noise reduction using Median Blur, particularly effective for salt-and-pepper noise.*

---

### **5. Bilateral Filter Results**  
![Bilateral Filter Results](screenshots/Bilateral_Filter.png)  
*Noise reduction using Bilateral Filtering while preserving edges.*

---

### **6. Edge Detection Results**  
![Edge Detection Results](screenshots/Edge_Detection.png)  
*Detection of edges in the processed image using the Canny edge detection algorithm.*

---

### **7. Object Detection Results**  
![Object Detection Results](screenshots/Object_Detection.png)  
*Highlighted objects detected in the underwater image with their respective labels and confidence scores.*

---

### **8. Histogram Visualization**  
![Histogram Visualization](screenshots/Histogram.png)  
*A histogram of the grayscale image with Otsu's threshold value marked for optimal thresholding.*

---

### **9. Comparison of Edge Detection Techniques**  
![Edge Detection Comparison](screenshots/Edge_Detection_Comparison.png)  
*A comparison of edge pixel counts for images processed using different noise reduction techniques, visualized as a bar chart.*

---
Yes, you should absolutely add credits to the dataset you used from Kaggle. Giving proper credit demonstrates ethical project practices and acknowledges the contribution of the dataset creators. It also helps others reproduce or further explore your work.

Here’s how you can add the credits in your README:

---

### **Dataset**
The model used in this project was trained using a dataset sourced from **Kaggle**. Special thanks to [**a3amat02**](https://www.kaggle.com/a3amat02) for providing valuable data for underwater image analysis.  
- **Dataset Name**: Underwater Plastic Garbage Detection || YOLOv8  
- **Link**: [Dataset URL](https://www.kaggle.com/code/a3amat02/underwater-plastic-garbage-detection-yolov8)

---

## **Author**

Created with ❤️ by **Shubhankar Sarkar**.  
[GitHub Profile](https://github.com/shubhankar05sarkar)

---

