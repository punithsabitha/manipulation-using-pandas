import pandas as pd

# Create dictionary
data = {
    "Name": ["Pankaj", "Meghna", "David", "Lisa"],
    "Role": ["CEO", None, None, None],
    "Salary": [100, 200, None, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print initial 2 rows
print("First 2 rows:")
print(df.head(2))

# Print last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# Total null values
print("\nTotal Null Values:")
print(df.isnull().sum().sum())

# Detailed information
print("\nDataFrame Info:")
print(df.info())

# Drop rows with null values
df_no_null_rows = df.dropna()
print("\nAfter Dropping Rows with Null Values:")
print(df_no_null_rows)

# Drop columns with null values
df_no_null_cols = df.dropna(axis=1)
print("\nAfter Dropping Columns with Null Values:")
print(df_no_null_cols)

# Fill Salary null values with 300
df["Salary"].fillna(300, inplace=True)
print("\nAfter Filling Salary Null Values:")
print(df)

# Fill Role null values with CEO
df["Role"].fillna("CEO", inplace=True)
print("\nAfter Filling Role Null Values:")
print(df)
