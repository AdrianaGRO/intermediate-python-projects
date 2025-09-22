import numpy as np
from PIL import Image
import os

class Canvas:
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = color

    def make_pixel(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        # Use current directory for simplicity
        img.save(image_path)
        
    def clear(self):
        """Reset the canvas to the original background color"""
        self.data[:] = self.color
