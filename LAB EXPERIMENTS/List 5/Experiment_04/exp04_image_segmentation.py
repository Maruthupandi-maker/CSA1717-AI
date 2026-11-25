"""
Experiment 04: Image Segmentation using Computer Vision Thresholding & K-Means
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np

# Create a synthetic 6x6 grayscale image with background (30) and foreground object (210)
image = np.array([
    [25, 30, 28, 32, 29, 26],
    [31, 205, 215, 210, 200, 30],
    [28, 220, 225, 218, 212, 27],
    [30, 208, 214, 219, 204, 29],
    [27, 29, 31, 28, 30, 25],
    [26, 28, 27, 30, 29, 24]
], dtype=np.uint8)

# Otsu-style binary threshold segmentation
threshold = 120
segmented_mask = (image > threshold).astype(int)

print("=== Original Grayscale Pixel Matrix ===")
print(image)
print(f"\n=== Segmented Binary Mask (Threshold = {threshold}) ===")
print(segmented_mask)
print(f"\nForeground Pixels: {np.sum(segmented_mask == 1)} | Background Pixels: {np.sum(segmented_mask == 0)}")
