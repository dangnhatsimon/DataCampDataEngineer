# Create the clean_string function
def clean_string(text):
  
    # Replace spaces with underscores
    no_spaces = text.replace(" ", "_")
    
    # Convert to lowercase
    clean_text = no_spaces.lower()
    
    # Return the final text as an output
    return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)


password = "not_very_secure_2023"

# Define the password_checker function
def password_checker(submission):
  
    # Check that the password variable and the submission match
    if submission == password:
      print("Successful login!")
    
    # Otherwise, print "Incorrect password"
    else:
      print("Incorrect password")

# Call the function    
password_checker("NOT_VERY_SECURE_2023")

# Define clean_text
def clean_text(text, lower=True):
    if lower == False:
      clean_text = text.replace(" ", "_")
      return clean_text
    else:
      clean_text = text.replace(" ", "_")
      clean_text = clean_text.lower()
      return clean_text

# Define clean_text
def clean_text(text, remove=None):
    if remove != None:
      clean_text = text.replace(remove, "")
      clean_text = clean_text.lower()
      return clean_text
    else:
      clean_text = text.lower()
      return clean_text


# Create the convert_data_structure function
def convert_data_structure(data, data_type="list"):
  
    # If data_type is "tuple"
    if data_type == "tuple":
      data = tuple(data)
    
    # Else if data_type is set, convert to a set
    elif data_type == "set":
      data = set(data)
    else:
      data = list(data)
    return data

# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")



def clean_string(text):
  
    # Add a single-line docstring
    """Swap spaces to underscores and convert text to lowercase."""
    
    no_spaces = text.replace(" ", "_")
    clean_text = no_spaces.lower()
    return clean_text

# Access the docstring
print(clean_string.__doc__)



# Create the convert_data_type function
def convert_data_structure(data, data_type="list"):
    # Add a multi-line docstring
    """
    Convert a data structure to a list, tuple, or set.
    
    Args:
      data (list, tuple, or set): A data structure to be converted.
      data_type (str): String representing the type of structure to convert data to.
      
    Returns:
      data (list, tuple, or set): Converted data structure.
    """
    if data_type == "tuple":
      data = tuple(data)
    elif data_type == "set":
      data = set(data)
    else:
      data = list(data)
    return data

print(help(convert_data_structure))



# Define a function called concat
def concat(*args):
    
    # Create an empty string
    result = ""
    
    # Iterate over the Python args tuple
    for arg in args:
      result += " " + arg
    return result

# Call the function
print(concat("Python", "is", "great!"))


# Define a function called concat
def concat(**kwargs):
    
    # Create an empty string
    result = ""
    
    # Iterate over the Python kwargs
    for kwarg in kwargs.values():
      result += " " + kwarg
    return result

# Call the function
print(concat(start="Python", middle="is", end="great!"))