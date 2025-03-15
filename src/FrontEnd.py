import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ImageConfidenceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Confidence App")
        self.root.geometry("400x400")  # Set the window size to 400x400

        # Load and display image
        self.image = Image.open("C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_Repo\\CEC2025\\created_testing_data\\no__19.png")
        self.image = self.image.resize((224, 224), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.grid(row=0, column=1, padx=10, pady=10)

        # Display image name
        self.image_name_label = tk.Label(root, text="Image Name")
        self.image_name_label.grid(row=1, column=1, padx=10, pady=5)

        # Confidence bar
        self.confidence_var = tk.DoubleVar()
        self.confidence_bar = ttk.Progressbar(root, orient="vertical", length=224, mode="determinate", variable=self.confidence_var)
        self.confidence_bar.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

        # Yes/No box
        self.result_label = tk.Label(root, text="Yes", bg="green", font=("Arial", 24), width=10, height=2)
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Update confidence and result
        self.update_confidence(75)  # Example confidence value

    def update_confidence(self, confidence):
        self.confidence_var.set(confidence)
        if confidence >= 65:
            self.result_label.config(text="Yes", bg="green")
        else:
            self.result_label.config(text="No", bg="red")

    def update_image(self, image_path, confidence, file_name):
        # Load and display new image
        self.image = Image.open(image_path)
        self.image = self.image.resize((224, 224), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)
        self.image_label.image = self.photo  # Keep a reference to avoid garbage collection

        # Update image name
        self.image_name_label.config(text=file_name)

        # Update confidence and result
        self.update_confidence(confidence)

        

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConfidenceApp(root)

    # Example of updating the image, confidence, and file name at runtime
    app.update_image("C:\\Users\\laure\\OneDrive\\Documents\\CEC_2025\\CEC_2025\\train\\yes\\yes__151.png", 85, "yes__151.png")

    root.mainloop()