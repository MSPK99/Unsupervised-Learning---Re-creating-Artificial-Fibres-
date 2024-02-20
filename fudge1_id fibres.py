import os
from skimage.io import imread, imsave
from skimage.measure import label, regionprops
from skimage.color import rgb2gray, label2rgb
import numpy as np

# Set the directory containing the segmented images
segmented_dir = 'phase4_fibers'

# Set the directory for saving labeled images
labeled_dir = 'labeled_fibers'

# Create the directory if it doesn't exist
os.makedirs(labeled_dir, exist_ok=True)

# Iterate over the images in the directory
for filename in os.listdir(segmented_dir):
    if filename.endswith(".png"):
        print(f"Processing {filename}...")
        try:
            # Load the image
            img = imread(os.path.join(segmented_dir, filename))

            # If the image is not grayscale, convert it to grayscale
            if len(img.shape) == 3:
                img = rgb2gray(img)

            # Label the image
            label_image = label(img > 0)  # assuming the fibers are non-zero pixels

            # Count the number of fibers
            regions = regionprops(label_image)
            num_fibers = len(regions)
            print(f"Number of fibers in {filename}: {num_fibers}")

            # Convert the labeled image to RGB
            rgb_label_image = label2rgb(label_image, image=img)

            # Convert the image data to 8-bit unsigned integer format
            rgb_label_image = (rgb_label_image * 255).astype(np.uint8)

            # Save the labeled image
            imsave(os.path.join(labeled_dir, f"labeled_{filename}"), rgb_label_image)

        except Exception as e:
            print(f"Skipping {filename} due to an error: {e}")


