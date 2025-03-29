import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from preprocessing import to_grayscale, reduce_noise_gaussian, reduce_noise_median, reduce_noise_bilateral
from segmentation import detect_edges
from utils import show_images, plot_edge_counts, plot_histogram_with_threshold
from model import detect_and_draw  # We use detect_and_draw for detection with bounding boxes

class AquaLensApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AquaLens - Professional Marine Image Enhancer")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f2f6fc')

        self.image_path = None
        self.original_image = None  # Image in BGR format loaded via OpenCV
        self.processed_images = {}

        self.style = ttk.Style()
        self.configure_styles()
        self.create_widgets()

    def configure_styles(self):
        self.style.theme_use('clam')
        self.style.configure('TButton',
                             font=('Helvetica', 10, 'bold'),
                             padding=5,
                             background='#4a90e2',
                             foreground='white',
                             borderwidth=0)
        self.style.map('TButton',
                       background=[('active', '#357abd')],
                       relief=[('active', 'groove')])
        self.style.configure('TLabel',
                             background='#f2f6fc',
                             font=('Helvetica', 12),
                             foreground='#34495e')
        self.style.configure('Header.TLabel',
                             font=('Helvetica', 26, 'bold'),
                             foreground='#2c3e50')
        self.style.configure('TFrame', background='#f2f6fc')

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill='both', expand=True)

        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill='x', pady=(0, 20))
        ttk.Label(header_frame, text="AquaLens", style='Header.TLabel').pack()

        control_frame = ttk.LabelFrame(main_frame, text="Controls", padding=10, relief='ridge', style='TFrame')
        control_frame.pack(fill='x', pady=(0, 20))

        file_frame = ttk.Frame(control_frame)
        file_frame.pack(fill='x', pady=5)
        ttk.Button(file_frame, text="Load Image", command=self.load_image, width=15).pack(side='left', padx=5)
        self.status_label = ttk.Label(file_frame, text="No image loaded", foreground='#7f8c8d')
        self.status_label.pack(side='left', padx=10)

        processing_frame = ttk.Frame(control_frame)
        processing_frame.pack(fill='x', pady=10)

        # List of processing buttons including the new "Histogram" button and "Detect"
        buttons = [
            ("Grayscale", self.apply_grayscale),
            ("Gaussian Blur", self.apply_gaussian_blur),
            ("Median Blur", self.apply_median_blur),
            ("Bilateral Filter", self.apply_bilateral_filter),
            ("Edge Detection", self.apply_edge_detection),
            ("Compare Edges", self.plot_edge_comparison),
            ("Detect", self.run_detection),
            ("Histogram", self.run_histogram)
        ]
        for idx, (text, command) in enumerate(buttons):
            ttk.Button(processing_frame, text=text, command=command, width=15).grid(row=0, column=idx, padx=5)

        # Image Preview Area
        display_frame = ttk.LabelFrame(main_frame, text="Image Preview", padding=10, relief='ridge', style='TFrame')
        display_frame.pack(fill='both', expand=True)
        self.canvas = tk.Canvas(display_frame, bg='white')
        self.canvas.pack(fill='both', expand=True)
        self.image_label = ttk.Label(self.canvas)
        self.image_label.pack(expand=True)

        # Footer with Reset and Zoom controls
        footer_frame = ttk.Frame(main_frame)
        footer_frame.pack(fill='x', pady=(20, 0))
        ttk.Button(footer_frame, text="Reset", command=self.reset_app, width=15).pack(side='left', padx=5)
        self.zoom_var = tk.DoubleVar(value=1.0)
        zoom_scale = ttk.Scale(footer_frame, from_=0.5, to=2.0, variable=self.zoom_var,
                               command=self.update_zoom, length=200)
        zoom_scale.pack(side='right', padx=5)
        ttk.Label(footer_frame, text="Zoom:").pack(side='right')

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.image_path = path
            self.original_image = cv2.imread(self.image_path)
            if self.original_image is None:
                messagebox.showerror("Error", "Unable to load the selected image.")
                return
            self.processed_images.clear()
            self.status_label.config(text=f"Loaded: {path.split('/')[-1]}")
            self.display_image(self.original_image)

    def display_image(self, image):
        """
        Display the image on the canvas. We scale down the image to fit within the canvas,
        but never upscale it to preserve the original pixel quality.
        """
        # Convert image to RGB for display
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image_rgb)

        canvas_width = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 900
        canvas_height = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 500
        img_width, img_height = pil_image.size

        # Calculate scale factor; don't upscale beyond original size: use min(1, factor)
        factor = min(canvas_width / img_width, canvas_height / img_height)
        scale = min(1, factor * self.zoom_var.get())

        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        resized = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

    def apply_grayscale(self):
        if not self.check_image_loaded():
            return
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        self.processed_images['grayscale'] = gray_bgr
        self.display_image(gray_bgr)

    def apply_gaussian_blur(self):
        if not self.check_image_loaded():
            return
        if 'grayscale' not in self.processed_images:
            self.apply_grayscale()
        blurred = cv2.GaussianBlur(self.processed_images['grayscale'], (7, 7), 0)
        self.processed_images['gaussian'] = blurred
        self.display_image(blurred)

    def apply_median_blur(self):
        if not self.check_image_loaded():
            return
        if 'grayscale' not in self.processed_images:
            self.apply_grayscale()
        blurred = cv2.medianBlur(self.processed_images['grayscale'], 7)
        self.processed_images['median'] = blurred
        self.display_image(blurred)

    def apply_bilateral_filter(self):
        if not self.check_image_loaded():
            return
        if 'grayscale' not in self.processed_images:
            self.apply_grayscale()
        filtered = cv2.bilateralFilter(self.processed_images['grayscale'], 15, 100, 100)
        self.processed_images['bilateral'] = filtered
        self.display_image(filtered)

    def apply_edge_detection(self):
        if not self.check_image_loaded():
            return
        if 'grayscale' not in self.processed_images:
            self.apply_grayscale()
        edges = cv2.Canny(self.processed_images['grayscale'], 50, 150)
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        self.processed_images['edges'] = edges_bgr
        self.display_image(edges_bgr)

    def plot_edge_comparison(self):
        if not self.processed_images:
            messagebox.showwarning("Warning", "Please process the image first.")
            return
        images = []
        titles = []
        for key, img in self.processed_images.items():
            if key != 'edges':
                images.append(img)
                titles.append(key.capitalize())
        plot_edge_counts(images, titles)

    def run_detection(self):
        """
        Run YOLO detection on the loaded image and display the image with bounding boxes.
        """
        if not self.check_image_loaded():
            return
        detection_img = detect_and_draw(self.original_image)
        detection_img_rgb = cv2.cvtColor(detection_img, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(detection_img_rgb)

        # Use the same scaling logic as display_image (only downscaling)
        canvas_width = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 900
        canvas_height = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 500
        img_width, img_height = pil_image.size
        factor = min(canvas_width / img_width, canvas_height / img_height)
        scale = min(1, factor * self.zoom_var.get())
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        resized = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

    def run_histogram(self):
        """
        Convert the loaded image to grayscale and display its histogram along with the optimal threshold.
        """
        if not self.check_image_loaded():
            return
        # Convert image to grayscale
        gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        from utils import plot_histogram_with_threshold
        plot_histogram_with_threshold(gray_image)

    def check_image_loaded(self):
        if self.original_image is None:
            messagebox.showwarning("Warning", "Please load an image first.")
            return False
        return True

    def reset_app(self):
        self.processed_images.clear()
        if self.original_image is not None:
            self.display_image(self.original_image)

    def update_zoom(self, event=None):
        if self.original_image is not None:
            self.display_image(self.original_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = AquaLensApp(root)
    root.mainloop()
