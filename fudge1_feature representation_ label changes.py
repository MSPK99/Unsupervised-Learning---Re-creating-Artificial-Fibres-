import pandas as pd
import re

# Load the feature vectors
features = pd.read_excel('feature_vectors.xlsx')

# Extract the labels from the 'Image' column
features['Label'] = features['Image'].str.replace('labeled_fibers_', '').str.replace('.png', '')

# Remove the numbers and underscores from the labels
features['Label'] = features['Label'].apply(lambda x: re.sub(r'\d+', '', x).replace('_', '').strip())

# Save the feature vectors with labels to a new Excel file
features.to_excel('feature_vectors_with_labels.xlsx', index=False)

print('Saved the feature vectors with labels to feature_vectors_with_labels.xlsx.')
