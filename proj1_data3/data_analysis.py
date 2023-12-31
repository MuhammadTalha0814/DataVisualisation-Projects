# -*- coding: utf-8 -*-
"""Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kK5t0u65IiH4Jj_M8T2UDjZypG9ENcI2
"""

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Load the data from CSV 

# Set path as this 
data = pd.read_csv('proj1_data1 (1).csv')
# data = pd.read_csv('proj1_data2.csv') 
# use this for dataset2

# data = pd.read_csv('proj1_data3.csv') 
# use this for dataset3


# Display the loaded data
print("Loaded data:")
print(data)

# Skill 1: Extract a column as a NumPy array
column_data = data['DLC'].to_numpy()
print("\nDLC column as NumPy array:")
print(column_data)

# Skill 2: Calculate statistics using NumPy
mean_dlc = np.mean(column_data)
median_dlc = np.median(column_data)
std_dlc = np.std(column_data)
print("\nStatistics of DLC column:")
print("Mean:", mean_dlc)
print("Median:", median_dlc)
print("Standard Deviation:", std_dlc)

# Skill 3: Filter data using NumPy's where function
data['Arbitration_ID'] = pd.to_numeric(data['Arbitration_ID'], errors='coerce')
filtered_data = data[data['Arbitration_ID'] > 300]
print("\nFiltered data based on Arbitration_ID:")
print(filtered_data)

# Skill 4: Perform matrix manipulation with NumPy
matrix = np.array(data[['DLC', 'Arbitration_ID']])
transposed_matrix = np.transpose(matrix)
print("\nTransposed matrix:")
print(transposed_matrix)

# Skill 5: Vectorized computation using NumPy
result = column_data + 10
print("\nDLC column incremented by 10:")
print(result)