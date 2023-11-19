import pandas as pd
import os

# Data for the three reports
data1 = {
    "Product": ["Laptop", "Smartphone", "Tablet"],
    "Price": ["$999", "$499", "$299"],
    "Date Added": ["2023-01-15", "2023-02-01", "2023-02-20"],
    "Category": ["Electronics", "Electronics", "Electronics"]
}

data2 = {
    "Product": ["Coffee Mug", "Tea Set", "Cutlery Set"],
    "Price": ["$15", "$45", "$85"],
    "Date Added": ["2023-03-05", "2023-03-15", "2023-04-01"],
    "Category": ["Kitchenware", "Kitchenware", "Kitchenware"]
}

data3 = {
    "Product": ["Book", "Journal", "Pen Set"],
    "Price": ["$12", "$8", "$5"],
    "Date Added": ["2023-03-10", "2023-03-20", "2023-04-05"],
    "Category": ["Stationery", "Stationery", "Stationery"]
}

# Creating DataFrames from the data
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the data directory path
data_dir = os.path.join(script_dir, 'data')

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# File paths for the CSV files
report1_path = os.path.join(data_dir, 'scraped_report1.csv')
report2_path = os.path.join(data_dir, 'scraped_report2.csv')
report3_path = os.path.join(data_dir, 'scraped_report3.csv')

# Save the files
df1.to_csv(report1_path, index=False)
df2.to_csv(report2_path, index=False)
df3.to_csv(report3_path, index=False)
