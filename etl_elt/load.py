def transform(raw_data):
	# Find the items prices less than 25 dollars
	return raw_data.loc[raw_data["Price Each"] < 25, ["Order ID", "Product", "Price Each", "Order Date"]]

def load(clean_data):
	# Write the data to a CSV file without the index column
	clean_data.to_csv("transformed_sales_data.csv", index=False)


clean_sales_data = transform(raw_sales_data)

# Call the load function on the cleaned DataFrame
load(clean_sales_data)




# Import the os library
import os

# Load the data to a csv file with the index, no header and pipe separated
def load(clean_data, path_to_write):
	clean_data.to_csv(path_to_write, header=False, sep="|")

load(clean_sales_data, "clean_sales_data.csv")

# Check that the file is present.
file_exists = os.path.exists("clean_sales_data.csv")
print(file_exists)




def load(clean_data, file_path):
    # Write the data to a file
    clean_data.to_csv(file_path, header=False, index=False)

    # Check to make sure the file exists
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load(clean_sales_data, "transformed_sales_data.csv")
