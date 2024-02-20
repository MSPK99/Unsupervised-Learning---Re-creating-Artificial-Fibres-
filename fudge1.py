import os
from skimage import feature, io, util, exposure
import numpy as np
from PIL import Image, ImageEnhance
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square, disk, dilation
from skimage.color import label2rgb
from skimage.transform import hough_line, hough_line_peaks
from skimage.feature import canny
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

# Phase 1: Enhance the contrast of the images
input_folder = "piezo1"
output_folder_phase1 = "phase1_enhanced"
output_folder_phase2 = "phase2_ridges"
output_folder_phase3 = "phase3_segmented"
output_folder_phase4 = "phase4_fibers"

if not os.path.exists(output_folder_phase1):
    os.makedirs(output_folder_phase1)

if not os.path.exists(output_folder_phase2):
    os.makedirs(output_folder_phase2)

if not os.path.exists(output_folder_phase3):
    os.makedirs(output_folder_phase3)

if not os.path.exists(output_folder_phase4):
    os.makedirs(output_folder_phase4)

for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        print(f"Processing {filename}...")
        try:
            # Open the image file
            img = Image.open(os.path.join(input_folder, filename))
            # Enhance the contrast of the image
            enhancer = ImageEnhance.Contrast(img)
            enhanced_img = enhancer.enhance(1.5)
            # Convert the image mode back to 'L' before saving
            enhanced_img = enhanced_img.convert('L')
            # Save the enhanced image
            enhanced_img.save(os.path.join(output_folder_phase1, f"enhanced_{filename}"))
            print(f"Saving the enhanced image to {output_folder_phase1}\\enhanced_{filename}...")

            # Phase 2: Ridge detection
            # Convert the enhanced image to a numpy array
            img_array = np.array(enhanced_img)
            # Perform edge detection
            edges = feature.canny(img_array, sigma=2.5)
            # Convert the edges to an image
            edges_img = Image.fromarray(edges)
            # Save the edges image
            edges_img.save(os.path.join(output_folder_phase2, f"edges_{filename}"))
            print(f"Saving the edges image to {output_folder_phase2}\\edges_{filename}...")

            # Phase 3: Segmentation
            # Open the image file
            img = io.imread(os.path.join(output_folder_phase2, f"edges_{filename}"), as_gray=True)
            # Apply Otsu's thresholding
            thresh = threshold_otsu(img)
            bw = closing(img > thresh, disk(3))
            # Remove artifacts connected to image border
            cleared = clear_border(bw)
            # Label image regions
            label_image = label(cleared)
            image_label_overlay = label2rgb(label_image, image=img)
            # Convert the image data to 8-bit unsigned integer format
            image_label_overlay = (image_label_overlay * 255).astype(np.uint8)
            # Save the segmented image
            io.imsave(os.path.join(output_folder_phase3, f"segmented_{filename}"), image_label_overlay)
            print(f"Saving the segmented image to {output_folder_phase3}\\segmented_{filename}...")

            # Phase 4: Fiber extraction
            # Open the image file
            img = io.imread(os.path.join(output_folder_phase3, f"segmented_{filename}"), as_gray=True)
            # Apply dilation
            dilated_img = dilation(img, disk(1.5))  # The size of the disk determines the amount of dilation
            # Save the dilated image
            io.imsave(os.path.join(output_folder_phase4, f"fibers_{filename}"), img_as_ubyte(dilated_img))
            print(f"Saving the fiber image to {output_folder_phase4}\\fibers_{filename}...")
        except Exception as e:
            print(f"Skipping {filename} due to an error: {e}")
