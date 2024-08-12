import pandas as pd

# Read the Excel file without headers
df = pd.read_excel('Movie Data.xlsx', header=None)
# Split the data into columns using the comma as a separator
# We only split from the second row (index 1)
df[['Movie Title', 'Release Year', 'Budget (millions $)', 'Rotten Tomatoes Score', 'Genre']] = df[0].str.split(',', expand=True)
# Remove the original column
df = df.drop(columns=[0])
# Remove the first row that contained the original headers
df = df.iloc[1:]
# Reset the indices
df.reset_index(drop=True, inplace=True)
# Display the resulting DataFrame
print(df)

# Show the number of rows and columns
print(df.shape)
# Show the columns of the DataFrame
print(df.columns)
# Show the first few rows of the DataFrame
print(df.head())
# Show information about the DataFrame
print(df.info())
# Show statistics about the DataFrame
print(df.describe())

# Show the number of categories and their unique values for each column
for column in df.columns:
    unique_categories = df[column].nunique()
    categories = df[column].unique()
    print(f"Column: {column}")
    print(f"Number of categories: {unique_categories}")
    print(f"Categories: {', '.join(map(str, categories))}")
    print()

    # Count the total for each category in the column
    category_counts = df[column].value_counts()
    print(f"Total for each category in the column {column}:")
    print(category_counts)
    print()
