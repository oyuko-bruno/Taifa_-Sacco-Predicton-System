import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of rows in the dataset
num_samples = 1000

# Generate synthetic data for each column
#this is so creative
data = {
    'Collateral': np.random.choice(['yes', 'no'], size=num_samples),
    'Government_Program': np.random.choice(['yes', 'no'], size=num_samples),
    'Loan_Purpose': np.random.choice(['purchase_equipment', 'expanding_operations', 'covering_operations_expenses'], size=num_samples),
    'Local_Economic_Factors': np.random.choice(['drought', 'rainy'], size=num_samples),
    'Risk_Management_Strategies': np.random.choice(['yes', 'no'], size=num_samples),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('loan_prediction_dataset.csv', index=False)

existing_data = pd.read_csv('train.csv')

# Load the synthetic dataset
synthetic_data = pd.read_csv('loan_prediction_dataset.csv')

# Concatenate the datasets vertically (along rows)
combined_data = pd.concat([existing_data, synthetic_data], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_data.to_csv('combined_dataset.csv', index=False)

# Display the first few rows of the generated dataset

