import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_preprocess_data(filepath):
    """
    Procedure to load and preprocess the student data.
    :param filepath: Path to the CSV file containing student data.
    :return: Tuple containing the DataFrame and training/validation sets.
    """
    pd.set_option('display.max_columns', None)

    # Load the dataset
    student_df = pd.read_csv(filepath)

    # Calculate average grade
    student_df['avg_G'] = student_df[['G1', 'G2', 'G3']].mean(axis=1)

    # Define features and target
    X = student_df.drop(columns=['id', 'G1', 'G2', 'G3', 'avg_G'])
    y = student_df['avg_G']

    # Split the data into training and testing sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

    return student_df, X_train, X_val, y_train, y_val
