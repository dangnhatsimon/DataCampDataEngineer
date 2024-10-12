# Import the string module
import string

# Print all ASCII lowercase characters
print(string.ascii_lowercase)

# Print all punctuation
print(string.punctuation)


# Import date from the datetime module
from datetime import date

# Create a variable called deadline
deadline = date(2024, 1, 19)

# Check the data type
print(type(deadline))

# Print the deadline
print(deadline)


# Import pandas as pd
import pandas as pd
# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_df.head())

# Read in sales.csv
sales_df = pd.read_csv("sales.csv")

# Print the mean order_value
print(sales_df["order_value"].mean())

# Print the total value of sales
print(sales_df["order_value"].sum())