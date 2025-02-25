from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter as tk
from tkinter import messagebox

# Set up tkinter root
root = tk.Tk()
root.withdraw()  # Hide the root window (dialog only)

# Open file dialog to select image
file_path = askopenfilename(title="Select an image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
if not file_path:  # Check if no file is selected
    messagebox.showerror("No File Selected", "You must select a file to compress.")
    exit()

try:
    # Open the image
    img = Image.open(file_path)

    # Get the original image size
    img_width, img_height = img.size

    # Compress by resizing image (reduce size by 50%)
    compressed_width = int(img_width * 0.5)
    compressed_height = int(img_height * 0.5)
    img = img.resize((compressed_width, compressed_height), Image.Resampling.LANCZOS)

    # Open save dialog to choose where to save compressed image
    save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")], title="Save Compressed Image")
    if not save_path:  # Check if no save path is selected
        messagebox.showerror("No Save Path", "You must select a path to save the file.")
        exit()

    # Save the compressed image with reduced quality
    img.save(save_path, format="JPEG", quality=70)  # 70% quality for good compression
    messagebox.showinfo("Compression Complete", f"Image compressed and saved to: {save_path}")

except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")