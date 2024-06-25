import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

matplotlib.use('Agg')  # Use a non-interactive backend

"""======================================
    Descriptive Methods for Data Dashboard
======================================"""


def save_sex_distribution_chart():
    """======================================
    Generate a pie chart: Distribution of Sex in the dataset

    Procedure will read dataset and generate a pie chart of the distribution from
    the raw data. The chart will be saved as a PNG file in the frontend/static folder.

    Parameters: None
    Returns None
    ========================================"""
    data = pd.read_csv('../data/student_data_raw.csv')
    logging.debug("Generating sex distribution chart")
    # Map 'M' to 'Male' and 'F' to 'Female'
    data['sex'] = data['sex'].map({'M': 'Male', 'F': 'Female'})

    # Count the occurrences of each sex
    sex_counts = data['sex'].value_counts()

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the pie chart
    plt.figure(figsize=(8, 6))
    colors = sns.color_palette('pastel')[0:len(sex_counts)]
    plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Distribution of Sex')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart1.png')
    plt.close()


def save_age_distribution_chart():
    """======================================
    Generate a scatter plot: Distribution of Age in the dataset

    Procedure will read dataset and generate a scatter plot of the distribution from
    the raw data. The chart will be saved as a PNG file in the frontend/static folder.

    Parameters: None
    Returns None
    ========================================"""
    data = pd.read_csv('../data/student_data_raw.csv')
    logging.debug("Generating age distribution chart")
    # Count the occurrences of each age
    age_counts = data['age'].value_counts()

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    colors = sns.color_palette('pastel')[0:len(age_counts)]
    plt.scatter(age_counts.index, age_counts, color=colors)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Distribution of Age')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart2.png')
    plt.close()


def save_study_time_distribution_chart():
    """======================================
    Generate a bar chart: Distribution of Study Time in the dataset

    Procedure will read dataset and generate a bar chart of the distribution from
    the raw data. The chart will be saved as a PNG file in the frontend/static folder.

    Parameters: None
    Returns None
    ========================================"""

    data = pd.read_csv('../data/student_data_raw.csv')

    # Count the occurrences of each study time
    study_time_counts = data['studytime'].value_counts()

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    colors = sns.color_palette('pastel')[0:len(study_time_counts)]
    plt.bar(study_time_counts.index, study_time_counts, color=colors)
    plt.xlabel('Study Time')
    plt.ylabel('Count')
    plt.title('Distribution of Study Time')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart3.png')
    plt.close()


def save_G1_distribution_chart():
    """======================================
     Generate a histogram: Distribution of G1 in the dataset

     Procedure will read dataset and generate a histogram of the grade distribution from
     the raw data from the first test. The chart will be saved as a PNG file in the frontend/static folder.

     Parameters: None
     Returns None
     ========================================"""

    data = pd.read_csv('../data/student_data_raw.csv')

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['G1'], kde=True, stat='density')
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Distribution of G1')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart4.png')
    plt.close()


def save_G2_distribution_chart():
    """======================================
    Generate a histogram: Distribution of G2 in the dataset

    Procedure will read dataset and generate a histogram of the grade distribution from
    the raw data from the second test. The chart will be saved as a PNG file in the frontend/static folder.

    Returns None
    Parameters: None
    ========================================"""
    data = pd.read_csv('../data/student_data_raw.csv')

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['G2'], kde=True, stat='density')
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Distribution of G2')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart5.png')
    plt.close()


def save_G3_distribution_chart():
    """======================================
    Generate a histogram: Distribution of G3 in the dataset

    Procedure will read dataset and generate a histogram of the grade distribution from
    the raw data from the third test. The chart will be saved as a PNG file in the frontend/static folder.

    Returns None
    Parameters: None
    ========================================"""
    data = pd.read_csv('../data/student_data_raw.csv')

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['G3'], kde=True, stat='density')
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Distribution of G3')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/chart6.png')
    plt.close()


def save_heat_maps():
    """======================================
    Generate a heatmap: Correlation between variables in the dataset

    Procedure will read dataset and generate a heatmap of the correlation between
    variables in the raw data. The chart will be saved as a PNG file in the frontend/static folder.

    Returns None
    Parameters: None
    ========================================"""
    df = pd.read_csv('../data/student_data_raw.csv')

    # Create a new column with the average grade from G1, G2, and G3
    df['average_grade'] = (df['G1'] + df['G2'] + df['G3']) / 3

    # Drop the G1, G2, and G3 columns
    df = df.drop(['G1', 'G2', 'G3'], axis=1)

    # One Hot Encoding for categorical variables
    df = pd.get_dummies(df)

    # Controllable Features

    controllable_features = [
        'average_grade',
        'studytime',
        'traveltime',
        'internet_no',
        'internet_yes',
        'paid_no',
        'paid_yes',
        'activities_no',
        'activities_yes',
        'schoolsup_no',
        'schoolsup_yes']

    # Uncontrollable Features Personal
    personal_features = [
        "average_grade",
        "age",
        "sex_F",
        "sex_M",
        "address_R",
        "address_U",
        "freetime",
        "goout",
        "absences",
        "romantic_no",
        "romantic_yes",
        "Dalc",
        "Walc",
        "health",
        "reason_course",
        "reason_home",
        "reason_other",
        "reason_reputation",
        "failures",
        "nursery_no",
        "nursery_yes",
        "higher_no",
        "higher_yes"
    ]

    # Uncontrollable Features Family
    family_features = [
        "average_grade",
        "famsize_GT3",
        "famsize_LE3",
        "famrel",
        "Medu",
        "Fedu",
        "Pstatus_A",
        "Pstatus_T",
        "Mjob_at_home",
        "Mjob_health",
        "Mjob_other",
        "Mjob_services",
        "Mjob_teacher",
        "Fjob_at_home",
        "Fjob_health",
        "Fjob_other",
        "Fjob_services",
        "Fjob_teacher",
        "guardian_father",
        "guardian_mother",
        "guardian_other",
        "famsup_no",
        "famsup_yes"
    ]

    # Create the correlation matrix
    corr_c = df[controllable_features].corr()
    corr_p = df[personal_features].corr()
    corr_f = df[family_features].corr()

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the heatmap controllable
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr_c, annot=True, cmap='coolwarm')
    plt.title('Correlation between Controllable Features')
    plt.savefig('../frontend/static/heatmap-c.png')
    plt.close()

    # Create the heatmap personal
    plt.figure(figsize=(30, 30))
    # Make the labels bigger
    sns.heatmap(corr_p, annot=True, cmap='coolwarm')

    # Increase overall font size to 1.5

    # Increase label size
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.xlabel('Features', fontsize=30)
    plt.ylabel('Features', fontsize=30)
    plt.title('Correlation between Personal Features', fontsize=30)
    plt.tight_layout()

    plt.title('Correlation between Personal Features')
    plt.savefig('../frontend/static/heatmap-p.png')
    plt.close()

    # Create the heatmap family
    plt.figure(figsize=(30, 30))  #
    sns.heatmap(corr_f, annot=True, cmap='coolwarm')
    # Increase Font Size
    plt.rcParams['font.size'] = 20
    # Increase label size
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.xlabel('Features', fontsize=30)
    plt.ylabel('Features', fontsize=30)
    plt.title('Correlation between Family Features', fontsize=30)
    plt.tight_layout()
    plt.title('Correlation between Family Features')
    plt.savefig('../frontend/static/heatmap-f.png')
    plt.close()


def save_study_time():
    """

    Returns
    -------

    """
    # Let's create some kind of line plot to show the correlation between study time and average grade
    df = pd.read_csv('../data/student_data_raw.csv')

    # Create a new column with the average grade from G1, G2, and G3
    df['average_grade'] = (df['G1'] + df['G2'] + df['G3']) / 3

    # Drop the G1, G2, and G3 columns
    df = df.drop(['G1', 'G2', 'G3'], axis=1)

    # Drop ages that are 20 or above
    df = df[df['age'] < 20]

    # Apply Seaborn styling
    sns.set(style="whitegrid")

    # Create the line plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='studytime', y='average_grade', data=df)
    plt.xlabel('Study Time')
    plt.ylabel('Average Grade')
    plt.title('Study Time vs. Average Grade')

    # Save the figure as a PNG file
    plt.savefig('../frontend/static/study-time.png')
    plt.close()
