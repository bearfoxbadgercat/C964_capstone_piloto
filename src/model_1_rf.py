import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
import joblib

pd.set_option('display.max_columns', None)

student_file_path = '../data/student_data_cleaned.csv'

# Step 1: Load the data
df = pd.read_csv(student_file_path)

# Step 2: Data Preparation
X = df.drop(['average_grade'], axis=1)
y = df['average_grade']

# Next split the data into training and testing sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

# Step 3: Model Training
# Let's build a random forest regression with control of leaves
rf = RandomForestRegressor(random_state=1, max_leaf_nodes = 11, max_depth=25,
                           min_weight_fraction_leaf=0.00, min_samples_leaf=15,
                           min_samples_split=2, n_estimators=200, n_jobs=-1, verbose=10)

# We need to train the model with some data to make predictions
rf.fit(X_train, y_train)

# Step 4: Model Evaluation
# Let's evaluate the model
y_pred = rf.predict(X_val)

# Calculate the mean absolute error
mae = mean_absolute_error(y_val, y_pred)
# Round the MAE to the nearest integer
mae = round(mae, 2)
print(f'Mean Absolute Error: {mae}')

# Step 5: Model Deployment
# Save the model to disk
joblib.dump(rf, '../model/rf_model.pkl')

# Load the model back from disk
rf_model = joblib.load('../model/rf_model.pkl')

