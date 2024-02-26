import pandas as pd

# Load the existing dataset
existing_data = pd.read_csv('train.csv')

# Load the synthetic dataset
synthetic_data = pd.read_csv('loan_prediction_dataset.csv')

# Concatenate the datasets vertically (along rows)
combined_data = pd.concat([existing_data, synthetic_data], ignore_index=True)

# Save the combined dataset to a new CSV file
combined_data.to_csv('combined_dataset.csv', index=False)
