# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
  
    # Check for values less than 25
    if value < 25:
        
        # Append the author to the list
        authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)


for genre, average_sale in genre_sales.items():
    
    # Filter for the maximum sales value
    if average_sale == 5166000000:
        
        # Print the genre
        print("Most popular genre: ", genre)
        print("Average sales: ", average_sale)
        
    # Filter for the minimum sales value
    elif average_sale == 80000000:
        
        # Print the genre
        print("Least popular genre: ", genre)
        print("Average sales: ", average_sale)


# Loop through the dictionary
for genre, sale in genre_sales.items():
  
    # Check if genre is Horror or Mystery
    if genre == "Horror" or genre == "Mystery":
        print(genre, sale)
    
    # Check if genre is Thriller and sale is at least 3 million
    elif genre == "Thriller" and sale>= 3000000:
        print(genre, sale)

