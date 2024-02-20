import pandas as pd
from sklearn.impute import SimpleImputer
from scipy.stats import zscore
import numpy as np

# Load the data
features = pd.read_excel('fiber_properties.xlsx')

# Define the columns to check for outliers
#outlier_columns = ['Length', 'Diameter', 'Orientation', 'Area']
outlier_columns = ['Length', 'Diameter', 'Orientation']

# Define the columns to fill missing values
#missing_value_columns = ['Length', 'Diameter', 'Orientation', 'Area']
missing_value_columns = ['Length', 'Diameter', 'Orientation']

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

# Save the cleaned data to a new Excel file
features.to_excel('fiber_properties_cleaned.xlsx', index=False)
print('Saved the cleaned data to fiber_properties_cleaned.xlsx.')
