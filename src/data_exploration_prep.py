# data_exploration_prep.py

"""
This module contains the following requirements from Part C:
    -  Ability to support featurizing, parsing, cleaning,  wrangling datasets
    -  Methods and algorithms supporting data exploration
    - Methods and algorithms supporting data preparation
    - Data visualization functionalities for data exploration and inspection
"""

# Importing necessary libraries
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# The very first step is to load the data
def load_data(file_path):
    """
    This method loads the data from the given file path
    :param file_path: The path to the file
    :return: The data in the form of a pandas dataframe
    """
    df = pd.read_csv(file_path)
    return df


def initial_data_exploration(df):
    """
    This method performs the initial data exploration
    :param df: The data in the form of a pandas dataframe
    :return: The first few rows of the data
    """
    return df.head().to_dict(orient='records')


def get_dataframe_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    return info


def num_stats_analysis(df):
    buffer = io.StringIO()
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    buffer.write("\nStatistics of numerical columns:\n")
    buffer.write(df[numerical_columns].describe().to_string())
    return buffer.getvalue()


def cat_column_analysis(df):
    buffer = io.StringIO()
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    buffer.write("\nUnique values in categorical columns:\n")
    for column in categorical_columns:
        unique_values = df[column].unique()
        buffer.write(f"{column}: {unique_values}\n")
    return buffer.getvalue()


def one_hot_encode(df):
    # One-hot encode the categorical columns using pandas get_dummies
    df = pd.get_dummies(df)
    # Let's average out the grades
    df['average_grade'] = df[['G1', 'G2', 'G3']].mean(axis=1)
    # Round the average_grade to the nearest whole number as int
    df['average_grade'] = df['average_grade'].apply(np.round).astype(int)
    # Let's drop the G1, G2, and G3 columns
    df.drop(['G1', 'G2', 'G3'], axis=1, inplace=True)
    # Let's drop id
    df.drop(['id'], axis=1, inplace=True)

    return df.head().to_dict(orient='records')


def controllable_heat_map(df):
    """
    This method creates a heatmap of the correlation matrix
    :param df: The data in the form of a pandas dataframe
    :return: The heatmap
    """
    # The list of features we want:
    controllable_factors = [
        "average_grade",
        "traveltime",
        "studytime",
        "internet_no",
        "internet_yes",
        "paid_no",
        "paid_yes",
        "activities_no",
        "activities_yes",
        "schoolsup_no",
        "schoolsup_yes"
    ]

    # Average the grades
    df['average_grade'] = df[['G1', 'G2', 'G3']].mean(axis=1)
    df['average_grade'] = df['average_grade'].apply(np.round).astype(int)
    df.drop(['G1', 'G2', 'G3'], axis=1, inplace=True)

    # One hot encode the data
    df = pd.get_dummies(df)

    # Create the heat map
    corr = df[controllable_factors].corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.show()


""""=========================================
Below we'll put the exploration and preparation methods
==========================================="""


# Part C: Methods and algorithms supporting data exploration
def explore_data():
    # Part C: Data visualization functionalities for data exploration and inspection

    pass


# Part C: Methods and algorithms supporting data preparation
def prepare_data():
    """
    This method prepares the data for the analysis
    It runs through all the steps required to clean the data
    per the exploratory data analysis from data pilot
    :return: None
    """
    # Part C:  Ability to support  parsing
    # Load the data
    file_path = "../data/student_data_raw.csv"

    df = load_data(file_path)

    # Part C: Ability to support featurizing
    # Combine G1, G2, and G3 into a single column averaged
    df['average_grade'] = df[['G1', 'G2', 'G3']].mean(axis=1)

    # Round the average_grade to the nearest whole number as an int
    df['average_grade'] = df['average_grade'].apply(np.round).astype(int)

    # Drop G1, G2, and G3 since we'll use the average_grade for better accuracy
    df.drop(['G1', 'G2', 'G3'], axis=1, inplace=True)

    # Drop id column
    df.drop(['id'], axis=1, inplace=True)

    # Part C: Ability to support cleaning
    # Drop rows where age is less than 20
    df = df[df['age'] < 20]

    # Drop features absences, freetime since little correlation
    df.drop(['absences', 'freetime'], axis=1, inplace=True)

    # Part C: Ability to support wrangling
    # One-hot encode the categorical columns using pandas get_dummies
    df = pd.get_dummies(df)

    # Save the cleaned dateset
    df.to_csv("../data/data_cleaned/student_data_cleaned.csv", index=False)
