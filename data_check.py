
import pandas as pd

# Load the dataset
df = pd.read_csv("news.csv")  # Change the filename if needed

# Display first 5 rows
print(df.head())

# Check if there are missing values
print("\nMissing values:\n", df.isnull().sum())
