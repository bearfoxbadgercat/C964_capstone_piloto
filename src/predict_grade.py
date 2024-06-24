import pandas as pd
import joblib

# Load the model back from disk
rf_model = joblib.load('../model/rf_model.pkl')

# Read in cleaned data
student_file_path = '../data/student_data_cleaned.csv'
all_students_df = pd.read_csv(student_file_path)

# Set the display options
pd.set_option('display.max_columns', None)


def get_student(df, row_number, model, studytime):
    # Make a copy of the row to avoid SettingWithCopyWarning
    student_df = df.iloc[[row_number]].copy()

    # Update the study time to the studytime provided
    student_df['studytime'] = studytime

    # Predict the grade
    grade = model.predict(student_df.drop(['average_grade'], axis=1))

    print(f"Predicted grade for student {row_number} with study time {studytime} is: {grade[0]}")


get_student(all_students_df, 1, rf_model, 5)
