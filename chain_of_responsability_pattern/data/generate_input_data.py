import pandas as pd

# Data for the reports
data = {
    "Product": ["Laptop", "Headphones", "Coffee Mug"],
    "Price": ["$999", "$199", "$15"],
    "Date Added": ["2023-01-15", "2023-02-20", "2023-03-05"],
    "Category": ["Electronics", "Electronics", "Kitchenware"]
}

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Report 1: Standard CSV format
df.to_csv('/data/report_standard.csv', index=False)

# Report 2: Key-Value Pair CSV format
df_key_value = df.apply(lambda x: '; '.join(x.index + ': ' + x), axis=1)
df_key_value.to_csv('/data/report_key_value.csv', index=False, header=False)

# Report 3: Pipe-separated CSV format without headers
df.to_csv('/data/report_pipe_delimited.csv', sep='|', index=False, header=False)


