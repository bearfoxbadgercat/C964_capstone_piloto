"""
File: data_handler.py
Author: Mike Castro
Updated: 04/23/2024

This file contains the DataHandler class, which is used to load, process, and save data for the project.
"""

# Let's import our libraries first
import pandas as pd
import numpy as np

# Shouldn't we read in the file yes or no?: Yes

# Let's read in the file:
df = pd.read_csv('../data/student_data_raw.csv')

print(df.head().to_string())