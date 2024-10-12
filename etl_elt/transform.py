# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] > 1, :]
    
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = clean_data[["Order Date", "Quantity Ordered", "Purchase Address"]]
    
    # Return the filtered DataFrame
    return clean_data
    
transform(raw_sales_data)



raw_sales_data = extract("sales_data.csv")

def transform(raw_data):
    # Convert the "Order Date" column to type datetime
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    
    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    return clean_data

clean_sales_data = transform(raw_sales_data)

# Check the data types of each column
print(clean_sales_data.dtypes)


def extract(file_path):
    raw_data = pd.read_parquet(file_path)
    return raw_data

raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Filter rows and columns
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] == 1, ["Order ID", "Price Each", "Quantity Ordered"]]
    return clean_data

# Transform the raw_sales_data
clean_sales_data = transform(raw_sales_data)