
''' Had to manually change a few labels so do not run this code again!!!!!!!!'''
import pandas as pd
import re

# Load the extracted features
features = pd.read_excel('fiber_properties_cleaned.xlsx')

# Remove the 'labeled_fibers_' prefix and '.png' suffix from the 'Image' column
features['Image'] = features['Image'].str.replace('labeled_fibers_', '').str.replace('.png', '')

# Group the features by image
grouped = features.groupby('Image')

# Compute statistical summaries of the features
summaries = grouped.agg(['mean', 'median', 'std', 'min', 'max', 'var'])

# Flatten the multi-level column index
summaries.columns = ['_'.join(col) for col in summaries.columns]

# Add a new column for the labels
summaries['Label'] = ''

# Iterate over the images in the DataFrame
for image in summaries.index:
    # Remove the date from the image name
    image_no_date = re.sub(r'\d{2}_\d{2}_\d{4}_', '', image)
    
    # Extract the label from the image name
    label = image_no_date.split('_')[0]
    
    # Assign the label to the corresponding image in the DataFrame
    summaries.loc[image, 'Label'] = label

# Save the feature vectors to a new Excel file
summaries.to_excel('feature_vectors.xlsx')

print('Saved the feature vectors to feature_vectors.xlsx.')