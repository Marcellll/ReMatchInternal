from os import path
from PIL import Image
import customtkinter as ctk
version = "v0.1.0"

def global_init(path):
    global path_name
    path_name = path

def resize_image(icon_path: str, image_width: int, image_height:int):
        try:
            image_path = path.abspath(path.join(path_name,icon_path))
            # Open the image
            original_image = Image.open(image_path)
            # Resize the image to fit the button
            resized_image = original_image.resize((image_width, image_height))
            # Convert the resized image to a Tkinter-compatible format
            return ctk.CTkImage(resized_image, resized_image)
        except Exception as e:
            print(f"Error loading or resizing image: {e}")