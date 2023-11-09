# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k,v in europe.items():
    print('the capital of {} is {}'.format(k,v))
    


# Import numpy as np
import numpy as np

# For loop over np_height
for x in np.nditer(np_height):
    print('{} inches'.format(x))

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)
    
    
    
    
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print('{}: {}'.format(lab,row['cars_per_cap']))
    
    
    
    
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for l,r in cars.iterrows():
    cars.loc[l,'COUNTRY']=r['country'].upper()

# Print cars
print(cars)




# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"]=cars['country'].apply(lambda x: x.upper())






