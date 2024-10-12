user_ids = ["T42YG4KTK", "VTQ39IDQ0", "CRL11YUWX", 
            "K6Y5URXLR", "V4XCBER7V", "IOGQWC61K"]

# Loop through user_ids
for  user_id in user_ids:
  # Print the user_id
    print(user_id)


# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for i in range(1, max_capacity+1):
  
    # Add one to tickets_sold in each iteration
    tickets_sold += 1
  
print("Sold out:", tickets_sold, "tickets sold!")



courses = {"LLM Concepts": "AI", 
           "Introduction to Data Pipelines": "Data Engineering", 
           "AI Ethics": "AI",
           "Introduction to dbt": "Data Engineering", 
           "Writing Efficient Python Code": "Programming",
           "Introduction to Docker": "Programming"}
# Loop through the dictionary's keys and values
for key, value in courses.items():
  
    # Check if the value is "AI"
    if value == "AI":
        print(key, "is an AI course")
  
    # Check if the value is "Programming"
    elif value == "Programming":
        print(key, "is a Programming course")
  
    # Otherwise, print that it is a "Data Engineering" course
    else:
        print(key, "is a Data Engineering course")
    


tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
    # Add one to tickets_sold in each iteration
    tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")



release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
    # Increment current_date by one
    current_date += 1
    
    # Promote purchases
    if current_date <= 24:
        print("Purchase before the 25th for early access")
    
    # Check if the date is equal to the 25th
    elif current_date == 25:
        print("Coming soon!")
    else:
        print("Available now!")
        

