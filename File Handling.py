# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:53:25 2023

@author: USER
"""
import numpy as np
data1_numpy1 = np.genfromtxt("Loan_prediction_dataset.csv", delimiter=",", filling_values=0)

#Extracting the 8th column that has the loan amount in it from the rest of the dataset 
loan_amounts = data1_numpy1[:, 8]

# Calculate mean, median, and standard deviation of loan amounts using NumPy functions
mean_amount = np.mean(loan_amounts)
median_amount = np.median(loan_amounts)
std_deviation = np.std(loan_amounts)

# Print the calculated statistical values
print(f"Mean of loan amounts: {mean_amount:.2f}")
print(f"Median of loan amounts: {median_amount:.2f}")
print(f"Standard deviation of loan amounts: {std_deviation:.2f}")