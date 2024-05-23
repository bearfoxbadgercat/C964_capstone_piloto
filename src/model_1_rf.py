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

pd.set_option('display.max_columns', None)

student_file_path = '../data/student_data_raw.csv'

student_df = pd.read_csv(student_file_path)
copy1_student_df = student_df.copya()

copy1_student_df['avg_G'] = copy1_student_df[['G1', 'G2', 'G3']].mean(axis=1)

# Let's drop any age that above 19 and store the results in copy2_student_df
copy2_student_df = copy1_student_df[copy1_student_df['age'] <= 19]

# let's define the feature 'X' by dropping the columns 'ID', 'G1', 'G2', 'G3', 'avg_G'
X = copy2_student_df.drop(['id', 'G1', 'G2', 'G3', 'avg_G'], axis=1)
y = copy2_student_df['avg_G']

# # Next split the data into training and testing sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

# Get list of categorical variables
s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)


# Apply one-hot encoder to each column with categorical data
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_val[object_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_val.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_val.drop(object_cols, axis=1)

# Add one-hot encoded columns to numerical features
OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

# Ensure all columns have string type
OH_X_train.columns = OH_X_train.columns.astype(str)
OH_X_valid.columns = OH_X_valid.columns.astype(str)

# Define the model. Set random_state to 1
model = RandomForestRegressor(random_state=1)

# Fit the model
model.fit(OH_X_train, y_train)

# Get the predicted G1 values
preds = model.predict(OH_X_valid)

# Calculate the mean absolute error of your Random Forest model on the validation data
mae = mean_absolute_error(y_val, preds)
print('Mean Absolute Error:', mae)


