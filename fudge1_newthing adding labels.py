import pandas as pd
import re
from sklearn.impute import SimpleImputer
from scipy.stats import zscore
import numpy as np

# Define a function to extract labels from the filename
def extract_label(filename):
    # List of possible labels
    labels = ["Yoda", "GFP", "KO", "YodatreatedGFP", "untreatedGFP", "WT", "GFP NG", "GFPstorm", "KO NG", "KO storm", "WT NG"]
    for label in labels:
        if label in filename:
            return label
    return None

# Load the data
features = pd.read_excel('fiber_properties_cleaned.xlsx')

# Extract labels and add them to a new column
features['Labels'] = features['Image'].apply(extract_label)

# Define the columns to check for outliers
outlier_columns = ['Length', 'Diameter']

# Define the columns to fill missing values
missing_value_columns = ['Length', 'Diameter']

# Create an imputer object with a mean filling strategy
imputer = SimpleImputer(strategy='mean')

# Apply the imputer to the columns with missing values
features[missing_value_columns] = imputer.fit_transform(features[missing_value_columns])

# Iterate over the columns
for col in outlier_columns:
    # Calculate the Z-scores
    z_scores = zscore(features[col])

    # Remove the outliers
    features = features[np.abs(z_scores) <= 3]

# Save the cleaned data with the added 'Labels' column to a new Excel file
features.to_excel('fiber_properties_with_labels_cleaned.xlsx', index=False)
print('Saved the cleaned data with labels to fiber_properties_with_labels_cleaned.xlsx.')



'''import pandas as pd
import re

# Load the feature vectors
features = pd.read_excel('feature_vectors_with_labels.xlsx')

# Define a function to extract the desired labels
def extract_label(image_name):
    # List of desired labels
    labels = ['GFP', 'KO', 'Yoda', 'WT']
    
    # Check if any of the desired labels are present in the image name
    for label in labels:
        if label in image_name:
            return label
    return None

# Extract the labels from the 'Image' column
features['Label'] = features['Image'].apply(extract_label)

# Save the feature vectors with labels to a new Excel file
features.to_excel('feature_vectors_with_labels_new.xlsx', index=False)

print('Saved the feature vectors with labels to feature_vectors_with_labels.xlsx.')
'''