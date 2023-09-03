# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium=cars[np.logical_and(cars['cars_per_cap']>=100,cars['cars_per_cap']<=500)]

# Print medium
print(medium)





# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])
print(cars.head(10))
# Print out observations for Australia and Egypt
print(cars.loc[(cars['country']=='Australia') | (cars['country']=='Egypt'),:])





# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])


# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['drives_right','cars_per_cap']])






# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[cars['country'].isin(['Russia','Morocco']),['country','drives_right']])
