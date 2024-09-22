import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

# Print the entire Series
print(s)

# Access specific elements
print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label (values: 20, 30, 40)

# Some useful properties and methods for Series:
print("Values as a NumPy array:", s.values) # Returns the Series data as a NumPy array
print("Index (labels):", s.index)           # Returns the index (labels) of the Series
print("Shape:", s.shape)                    # Returns a tuple representing the dimensions of the Series
print("Size:", s.size)                      # Returns the number of elements in the Series

# Summary statistics:
print("Mean:", s.mean())                    # Calculate the mean of the data
print("Sum:", s.sum())                      # Calculate the sum of the data
print("Min:", s.min())                      # Get the minimum value in the Series
print("Max:", s.max())                      # Get the maximum value in the Series

# Unique values:
print("Unique values:", s.unique())         # Get unique values
print("Number of unique values:", s.nunique()) # Get the number of unique values

# Sorting:
print("Sorted by values:", s.sort_values())   # Sort the Series by values
print("Sorted by index:", s.sort_index())     # Sort the Series by index labels

# Check for missing values:
print("Check for missing values:", s.isnull())  # Check for missing (NaN) values
print("Check for non-missing values:", s.notnull()) # Check for non-missing values

# Apply a custom function to each element:
print("Apply custom function (square values):", s.apply(lambda x: x**2))  # Square each value in the Series


import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)
print()

# Shape: Returns the dimensions of the DataFrame
print("Shape of DataFrame:")
print(df.shape)  # (number of rows, number of columns)
print()

# Info: Provides a concise summary, including data types and non-null values
print("Information about DataFrame:")
print(df.info())
print()

# Describe: Generates summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(df.describe())
print()

# Head and Tail: Displays the first or last n rows of the DataFrame
print("First row of DataFrame:")
print(df.head(1))  # Display the first row
print()

print("Last 4 rows of DataFrame:")
print(df.tail(4))  # Display the last 4 rows
print()

# Mean, Sum, Min, Max: Calculate summary statistics for each column
print("Mean of each column:")
print(df.mean(numeric_only=True))  # Mean only for numerical columns
print()

print("Sum of each column:")
print(df.sum(numeric_only=True))  # Sum only for numerical columns
print()

print("Min of each column:")
print(df.min(numeric_only=True))  # Min only for numerical columns
print()

print("Max of each column:")
print(df.max(numeric_only=True))  # Max only for numerical columns
print()

# Sort values: Sorts the DataFrame based on one or more columns
print("DataFrame sorted by 'Age':")
print(df.sort_values(by='Age'))
print()

# Group by: Groups data by 'City', useful for aggregations
print("Group by 'City':")
print(df.groupby('City').size())  # Shows the size of each group
print()

# Handle missing values, remove columns, or rename columns
# Adding some NaN values for demonstration
df_with_na = df.copy()
df_with_na.loc[1, 'Age'] = None  # Introduce NaN in 'Age'
df_with_na.loc[3, 'City'] = None  # Introduce NaN in 'City'

print("DataFrame with NaN values:")
print(df_with_na)
print()

print("DataFrame after filling NaN values with a default value (e.g., Age = 0, City = 'Unknown'):")
print(df_with_na.fillna({'Age': 0, 'City': 'Unknown'}))
print()

print("DataFrame after dropping rows with NaN values:")
print(df_with_na.dropna())
print()

print("DataFrame after renaming 'City' column to 'Location':")
print(df_with_na.rename(columns={'City': 'Location'}))
print()

# Apply: Apply a custom function across elements, rows, or columns
print("DataFrame with 'Name' column converted to uppercase:")
print(df.apply(lambda row: row['Name'].upper(), axis=1))
