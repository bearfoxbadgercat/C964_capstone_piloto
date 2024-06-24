"""
In this file we will create our initial dataset from the raw data.
This dataset will have minimal cleaning and preprocessing to create a baseline model.
1. Merge the three grades columns into one average grade column.
2. One-hot encode the categorical columns.

Then the dataset will be saved as a CSV file.

Steps to take:
Load the raw dataset.
Create a copy of the raw dataset to preserve the original data.
Calculate the average of the three grade columns and create a new column for the average grade.
Drop the original grade columns (grade 1, grade 2, and grade 3) from the dataset.
Apply one-hot encoding to the categorical columns.
Export the cleaned and preprocessed dataset to a CSV file using pandas.

"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# 1. Load the raw dataset.
file_path = '../data/student_data_raw.csv'
student_df = pd.read_csv(file_path)

# 2. Create a copy of the raw dataset to preserve the original data.
student_df_initial = student_df.copy()

# 3. Calculate the average of the three grade columns and create a new column for the average grade.
student_df_initial['avg_grade'] = student_df_initial[['G1', 'G2', 'G3']].mean(axis=1)

# 4. Drop the original grade columns (G1, G2, and G3) from the dataset.
student_df_initial.drop(columns=['G1', 'G2', 'G3'], inplace=True)

# 5. Apply one-hot encoding to the categorical columns using pd.get_dummies
student_df_initial = pd.get_dummies(student_df_initial) #

# # # 6. Export the cleaned and preprocessed dataset to a CSV file using pandas.
# output_file_path = '../data/student_data_initial.csv'
# student_df_initial.to_csv(output_file_path, index=False)

# Let's split the data into training and testing sets
X = student_df_initial.drop(columns=['avg_grade'])
y = student_df_initial['avg_grade']

# Split the data into training and testing sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

RandomForestRegressor(random_state=1)
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(X_train, y_train)

# Get the mean absolute error on the validation data
val_predictions = rf_model.predict(X_val)
val_mae = mean_absolute_error(y_val, val_predictions)

print(f"Validation MAE for Random Forest Model: {val_mae}")

# so say I want to predict with some new data I got from a new student and I want the features to be random
# I can do this by creating a new dataframe with random values
# I will create a new student with random values for the features

#print all columns
pd.set_option('display.max_columns', None)
print(X.head())


