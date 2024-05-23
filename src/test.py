from data_preprocessing import load_and_preprocess_data

# Filepath to the data
data_filepath = '../data/student_data_raw.csv'

# Load and preprocess data
student_df, X_train, X_val, y_train, y_val = load_and_preprocess_data(data_filepath)

# Access the DataFrame
print("DataFrame Head:")
# print(student_df.head())
print(student_df.sample(5))
