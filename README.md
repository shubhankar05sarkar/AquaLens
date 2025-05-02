# **AquaLens**

AquaLens is an innovative image processing application focused on enhancing underwater imagery to support marine monitoring and conservation efforts. The project employs advanced digital image processing techniques—such as converting images to grayscale, applying various noise reduction filters (Gaussian, Median, Bilateral), and using edge detection algorithms—to improve the clarity and quality of underwater images. This preprocessing not only makes the images visually clearer but also prepares them for subsequent analysis steps.

In addition, AquaLens integrates deep learning-based object detection using a YOLO (You Only Look Once) model to automatically identify objects in underwater scenes, such as plastic, debris, etc. The tool draws bounding boxes around detected objects and provides confidence scores, making it easier to quantify and analyze the objects present. To further support data-driven decision-making, the project includes visualization utilities that generate histograms (with Otsu’s thresholding) and compare edge detection results, offering insights into the image characteristics and processing effectiveness.

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
- **Programming Language:** Python  
- **Image Processing Libraries:** OpenCV and NumPy  
- **Visualization:** Matplotlib  
- **Graphical User Interface (GUI):** Tkinter  
- **Object Detection Model:** YOLO (via the Ultralytics YOLO library)    
- **Development Environment:** Visual Studio Code (and optionally Jupyter Notebook for testing non-GUI functionality)

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

## **Screenshots**

### **1. AquaLens GUI**  
![AquaLens GUI](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(1).png)  
*This is the main interface of AquaLens where users can upload and process underwater images.*

---

### **2. Grayscale Conversion Results**  
![Grayscale Conversion Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(6).png)  
*The result of converting an underwater image to grayscale for further processing.*

---

### **3. Gaussian Blur Results**  
![Gaussian Blur Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(7).png)  
*Noise reduction using Gaussian Blur to enhance image clarity.*

---

### **4. Median Blur Results**  
![Median Blur Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(8).png)  
*Noise reduction using Median Blur, particularly effective for salt-and-pepper noise.*

---

### **5. Bilateral Filter Results**  
![Bilateral Filter Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(9).png)  
*Noise reduction using Bilateral Filtering while preserving edges.*

---

### **6. Edge Detection Results**  
![Edge Detection Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(10).png)  
*Detection of edges in the processed image using the Canny edge detection algorithm.*

---

### **7. Object Detection Results**  
![Object Detection Results](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(11).png)  
*Highlighted objects detected in the underwater image with their respective labels and confidence scores.*

---

### **8. Histogram Visualization**  
![Histogram Visualization](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(13).png) 
*A histogram of the grayscale image with Otsu's threshold value marked for optimal thresholding.*

---

### **9. Comparison of Edge Detection Techniques**  
![Edge Detection Comparison](https://github.com/shubhankar05sarkar/AquaLens/blob/969d7deb641a1b681445ba5b1b475120a3b685fa/Screenshot%20(12).png)  
*A comparison of edge pixel counts for images processed using different noise reduction techniques, visualized as a bar chart.*

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

