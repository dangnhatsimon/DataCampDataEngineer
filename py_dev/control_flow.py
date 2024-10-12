# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
    print("Inflation decreased")

# Check if September inflation is more than August inflation
elif inflation_september > inflation_august:
    print("Inflation increased")
  
# Confirm that they are equal
else:
    print("Inflation remained stable")


min_num_beds = 2
min_sq_foot = 750
max_rent = 1900
# Check the number of beds
if num_beds < min_num_beds:
    print("Insufficient bedrooms")

# Check square feet
elif sq_foot <= min_sq_foot:
    print("Too small")

  
# Check the rent
elif rent > max_rent:
    print("Too expensive")

  
# If all conditions met
else:
    print("This looks promising!")
