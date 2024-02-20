'''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Load the dataset
# Please replace 'feature_vectors_with_labels.xlsx' with your actual file name
df = pd.read_excel('feature_vectors_with_labels.xlsx')

# Split the dataset into features and labels
X = df.drop('Label', axis=1)
y = df['Label']

# Identify non-numeric columns
non_numeric_columns = X.select_dtypes(include=['object']).columns

# Apply one-hot encoding to non-numeric columns
X = pd.get_dummies(X, columns=non_numeric_columns)

# Split the dataset into training and testing subsets again after preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train a logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Define the model
model = LogisticRegression()

# Define the parameters for tuning
parameters = {'penalty': ['l2', 'none'],
              'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
              'solver': ['newton-cg', 'lbfgs', 'sag']}

# Define the grid search
#grid_search = GridSearchCV(estimator=model, param_grid=parameters, cv=5, scoring='accuracy')

# Define the model and parameters
logistic = LogisticRegression()
parameters = {'C': [0.01, 0.1, 1, 10, 100], 'penalty': ['l1', 'l2'], 'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']}

# Fit the grid search to the data
#grid_search.fit(X_train, y_train)

# GridSearchCV
grid_search = GridSearchCV(estimator=logistic, param_grid=parameters, cv=5, scoring='accuracy', verbose=0)

# Now use the best parameters in the Logistic Regression model
best_params = {'C': 0.01, 'penalty': 'l2', 'solver': 'newton-cg'}

# Define the model with best parameters
logistic_best = LogisticRegression(C=best_params['C'], penalty=best_params['penalty'], solver=best_params['solver'])


# Get the best parameters
#best_parameters = grid_search.best_params_

# Print the best parameters
#print('Best Parameters:', best_parameters)
'''


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load the dataset
# Please replace 'feature_vectors_with_labels.xlsx' with your actual file name
df = pd.read_excel('feature_vectors_with_labels.xlsx')

# Split the dataset into features and labels
X = df.drop('Label', axis=1)
y = df['Label']

# Identify non-numeric columns
non_numeric_columns = X.select_dtypes(include=['object']).columns

# Apply one-hot encoding to non-numeric columns
X = pd.get_dummies(X, columns=non_numeric_columns)

# Scale the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing subsets again after preprocessing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Now use the best parameters in the Logistic Regression model
best_params = {'C': 0.01, 'penalty': 'l2', 'solver': 'newton-cg'}

# Define the model with best parameters
logistic_best = LogisticRegression(C=best_params['C'], penalty=best_params['penalty'], solver=best_params['solver'], max_iter=1000)

# Fit the model with the best parameters
logistic_best.fit(X_train, y_train)
