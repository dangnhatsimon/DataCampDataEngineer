import logging
import pandas as pd


def transform(raw_data):
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    
    # Create an info log regarding transformation
    logging.info("Transformed 'Order Date' column to type 'datetime'.")
    
    # Create debug-level logs for the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of the DataFrame after filtering: {clean_data.shape}")
    
    return clean_data
  
clean_sales_data = transform(raw_sales_data)


def extract(file_path):
    return pd.read_parquet(file_path)

# Update the pipeline to include a try block
try:
	# Attempt to read in the file
    raw_sales_data = extract("sales_data.parquet")
	
# Catch the FileNotFoundError
except FileNotFoundError as file_not_found:
	# Write an error-level log
	logging.error(file_not_found)


def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	# Attempt to transform DataFrame, log an info-level message
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")
	
except Exception:
	# Log a warning-level message
	logging.warning("Cannot filter DataFrame by 'Total Price'")


def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")

except KeyError as ke:
	logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")
	
	# Create the "Total Price" column, transform the updated DataFrame
	raw_sales_data["Total Price"] = raw_sales_data["Price Each"] * raw_sales_data["Quantity Ordered"]
	clean_sales_data = transform(raw_sales_data)
