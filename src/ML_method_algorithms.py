"""
This module contains the implementation of the machine-learning methods and algorithms used in the project.
    - Implementation of interactive queries (Back End)
    - Implementation of machine-learning methods and algorithms
    - Functionalities to evaluate the accuracy of the data product
    - Tools to monitor and maintain the product
"""
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

"""========================
Model Training
========================"""


# Part C : Tools to monitor and maintain the product
# Part C: Functionalities to evaluate the accuracy of the data product
# Part C: Implementation of machine-learning methods and algorithms

def create_rf_model(num_leafs):
    # Path to the directory where the model will be saved
    model_dir = '../models/'

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Convert num_leafs to integer
    num_leafs = int(num_leafs)

    # File path of cleaned data
    file_path = '../data/data_cleaned/student_data_cleaned.csv'

    # Load the data
    df = pd.read_csv(file_path)

    # Step 2: Assign the features and target variable
    X = df.drop(['average_grade'], axis=1)
    y = df['average_grade']

    # Step 3: Split the data into training and testing sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

    # Step 4: Instantiate the random forest model
    rf_model = RandomForestRegressor(random_state=1, max_depth=150,
                                     min_weight_fraction_leaf=0.00, min_samples_leaf=num_leafs,
                                     min_samples_split=2, n_estimators=150, n_jobs=-1, verbose=10)

    # We need to train the model with some data to make predictions
    rf_model.fit(X_train, y_train)

    # Next evaluate the model

    # Step 4: Model Evaluation
    # Let's evaluate the model
    y_pred = rf_model.predict(X_val)

    # Calculate the mean absolute error
    mae = mean_absolute_error(y_val, y_pred)
    # Round the MAE to the nearest integer
    mae = round(mae, 3)

    # Save the model with the directory path
    model_filename = os.path.join(model_dir, f'rf_model_{num_leafs}_leafs.joblib')
    joblib.dump(rf_model, model_filename)

    model_name = f'rf_model_{num_leafs}_leafs.joblib'

    # Return the model filename and the mean absolute error
    return mae, "\n\nModel saved as: \n" + model_name


# Part C: Implementation of machine-learning methods and algorithms


"""========================
Navigator
========================"""


# Part C: Predictive  Method
# Part C: Implementation of interactive queries
def predict_score(row_number, study_time, internet, activities, paid, model_name):
    # Print all columns in the head
    pd.set_option('display.max_columns', None)

    # First we should get the student from the raw data
    file_path1 = '../data/student_data_raw.csv'

    df = pd.read_csv(file_path1)

    # Get the student

    # Update studytime
    student = df.copy()

    # Update the student at row_number with the new values
    student.loc[row_number, 'studytime'] = study_time
    student.loc[row_number, 'internet'] = internet
    student.loc[row_number, 'activities'] = activities
    student.loc[row_number, 'paid'] = paid

    # Drop G1, G2, G3, absences, id, freetime
    student = student.drop(['absences'], axis=1)
    student = student.drop(['id'], axis=1)
    student = student.drop(['freetime'], axis=1)

    # One Hot Encode student
    student = pd.get_dummies(student)

    # Final step for student to be ready to be passed in to the model
    # Drop all rows that are not the row_number passed in
    student = student.drop(student.index[student.index != row_number])

    # Get student average grade
    average_grade = (student['G1'] + student['G2'] + student['G3']) / 3
    student = student.drop(['G1', 'G2', 'G3'], axis=1)
    print(student.head())

    # Load the model
    model_dir = '../models/'
    model_filename = os.path.join(model_dir, model_name)

    # Load the model
    model = joblib.load(model_filename)

    # Make a prediction and round it to 2 decimal places
    prediction = model.predict(student)

    return prediction
