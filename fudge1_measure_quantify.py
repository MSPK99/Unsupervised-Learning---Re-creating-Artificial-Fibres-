'''import os
import pandas as pd
from skimage.io import imread
from skimage.measure import label, regionprops
from skimage.color import rgb2gray

# Set the directory containing the segmented images
segmented_dir = 'labeled_fibers'

# Prepare an empty DataFrame to store the results
results = pd.DataFrame(columns=['Image', 'Fibre ID', 'Length'])

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

            # Compute the length of each fiber and store it in the DataFrame
            for i, region in enumerate(regions, start=1):
                length = region.major_axis_length
                results = results.append({'Image': filename, 'Fibre ID': i, 'Length': length}, ignore_index=True)

        except Exception as e:
            print(f'Skipping {filename} due to an error: {e}')

# Save the results to an Excel file
results.to_excel('fibre_lengths.xlsx', index=False)
print('Saved the results to fibre_lengths.xlsx.')
'''



'''import os
import pandas as pd
from skimage.io import imread
from skimage.measure import label, regionprops
from skimage.color import rgb2gray

# Set the directory containing the segmented images
segmented_dir = 'labeled_fibers'

# Initialize a list to store the data
data = []

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

            # Iterate over the regions, skipping the first two
            for i, region in enumerate(regions[2:], start=3):
                # Compute the length of the fiber
                length = region.major_axis_length

                # Append the data to the list
                data.append([filename, i, length])

        except Exception as e:
            print(f'Skipping {filename} due to an error: {e}')

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=['Image', 'Fiber ID', 'Length (pixels)'])

# Save the DataFrame to a CSV file
df.to_csv('fiber_lengths.csv', index=False)
'''



import os
import pandas as pd
from skimage.io import imread
from skimage.measure import label, regionprops, regionprops_table
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import watershed
from scipy import ndimage as ndi

# Set the directory containing the segmented images
segmented_dir = 'labeled_fibers'

# Prepare an empty DataFrame to store the results
results = pd.DataFrame()

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

            # Compute the properties of each fiber and store it in the DataFrame
            for i, region in enumerate(regions[2:], start=3):  # start from the third fiber
                length = region.major_axis_length
                diameter = region.minor_axis_length
                #orientation = region.orientation
                #area = region.area
                #fiber_data = {'Image': filename, 'Fibre ID': i, 'Length': length, 'Diameter': diameter, 'Orientation': orientation, 'Area': area}
                fiber_data = {'Image': filename, 'Fibre ID': i, 'Length': length, 'Diameter': diameter, 'Orientation': orientation}
                results = results.append(fiber_data, ignore_index=True)

            # Compute the total fiber density and connectivity
            fiber_density = len(regions) / (img.shape[0] * img.shape[1])
            connectivity = len(ndi.label(img)[1]) / len(regions)
            print(f'Fiber density in {filename}: {fiber_density}')
            print(f'Connectivity in {filename}: {connectivity}')

        except Exception as e:
            print(f'Skipping {filename} due to an error: {e}')

# Save the results to an Excel file
results.to_excel('fiber_properties.xlsx', index=False)
print('Saved the results to fiber_properties.xlsx.')
