'''import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.measure import label, regionprops
from skimage.color import rgb2gray, label2rgb

# Set the directory containing the segmented images
segmented_dir = 'reassigned_fibers'

# Set the directory for saving the images with overlaid fibre IDs
output_dir = 'labeled_fibers_with_ids'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the images in the directory
for filename in os.listdir(segmented_dir):
    if filename.endswith('.png'):
        print(f'Processing {filename}...')
        try:
            # Load the image
            img = imread(os.path.join(segmented_dir, filename))

            # If the image is not grayscale, convert it to grayscale
            if len(img.shape) == 3:
                img = rgb2gray(img)

            # Label the image
            label_image = label(img > 0)  # assuming the fibers are non-zero pixels

            # Compute the properties of the labeled regions
            regions = regionprops(label_image)

            # Create a labeled image for visualization
            image_label_overlay = label2rgb(label_image, image=img)

            # Create a new figure
            fig, ax = plt.subplots(figsize=(10, 6))

            # Display the image
            ax.imshow(image_label_overlay)

            # Overlay the fibre IDs
            for region in regions:
                # Get the coordinates of the centroid
                y, x = map(int, region.centroid)

                # Get the fibre ID
                fibre_id = region.label

                # Overlay the fibre ID on the image
                # Overlay the fibre ID on the image
                ax.text(x, y, str(fibre_id), color='yellow', fontsize=12)


            # Save the figure to the output directory
            fig.savefig(os.path.join(output_dir, f'with_ids_{filename}'))

            # Close the figure to free up memory
            plt.close(fig)

        except Exception as e:
            print(f'Skipping {filename} due to an error: {e}')

'''


import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
from skimage.measure import label, regionprops
from skimage.color import rgb2gray, label2rgb

# Set the directory containing the segmented images
segmented_dir = 'reassigned_fibers'

# Set the directory for saving the images with overlaid fibre IDs
output_dir = 'labeled_fibers_with_ids'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over the images in the directory
for filename in os.listdir(segmented_dir):
    if filename.endswith('.png'):
        print(f'Processing {filename}...')
        try:
            # Load the image
            img = imread(os.path.join(segmented_dir, filename))

            # If the image is not grayscale, convert it to grayscale
            if len(img.shape) == 3:
                img = rgb2gray(img)

            # Label the image
            label_image = label(img > 0)  # assuming the fibers are non-zero pixels

            # Compute the properties of the labeled regions
            regions = regionprops(label_image)

            # Create a labeled image for visualization
            image_label_overlay = label2rgb(label_image, image=img)

            # Create a new figure
            fig, ax = plt.subplots(figsize=(10, 6))

            # Display the image
            ax.imshow(image_label_overlay)

            # Overlay the fibre IDs
            for region in regions:
                # Get the coordinates of the first pixel in the region
                y, x = region.coords[0]

                # Get the fibre ID
                fibre_id = region.label

                # Overlay the fibre ID on the image
                ax.text(x, y, str(fibre_id), color='yellow', fontsize=12)

            # Save the figure to the output directory
            fig.savefig(os.path.join(output_dir, f'with_ids_{filename}'))

            # Close the figure to free up memory
            plt.close(fig)

        except Exception as e:
            print(f'Skipping {filename} due to an error: {e}')