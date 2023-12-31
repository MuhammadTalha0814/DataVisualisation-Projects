# -*- coding: utf-8 -*-
"""Data Visualisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dAuEbo5LfgvQ6MxcA2uqxMlDthJHRhgv
"""

import pandas as pd
import matplotlib.pyplot as plt


# Set path as this 
data = pd.read_csv('proj1_data1 (1).csv')
# data = pd.read_csv('proj1_data2.csv') 
# use this for dataset2

# data = pd.read_csv('proj1_data3.csv') 
# use this for dataset3


# Plot 1: Bar chart
plt.figure(figsize=(8, 6))
data['Class'].value_counts().plot(kind='bar')
plt.title('Distribution of Classes')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()
print()
print()

# Plot 2: Line chart
plt.figure(figsize=(10, 6))
timestamps = pd.to_datetime(data['Timestamp'], unit='s')
data['DLC'].plot(kind='line', color='blue')
plt.title('DLC Over Time')
plt.xlabel('Timestamp')
plt.ylabel('DLC')
plt.show()
print()
print()

# Plot 3: Histogram
plt.figure(figsize=(8, 6))
plt.hist(data['Arbitration_ID'], bins=20, edgecolor='black')
plt.title('Arbitration ID Histogram')
plt.xlabel('Arbitration ID')
plt.ylabel('Frequency')
plt.show()
print()
print()

# Plot 4: Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['DLC'], data['Arbitration_ID'], color='red', alpha=0.5)
plt.title('DLC vs Arbitration ID')
plt.xlabel('DLC')
plt.ylabel('Arbitration ID')
plt.show()
print()
print()


# Plot 5: Heatmap
plt.figure(figsize=(10, 8))
heatmap_data = data.pivot_table(index='SubClass', columns='Class', values='DLC', aggfunc='mean')
plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('DLC Heatmap')
plt.xlabel('Class')
plt.ylabel('SubClass')
plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)
plt.show()