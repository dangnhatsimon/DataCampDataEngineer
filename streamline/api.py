import pandas as pd
import requests

api_url = "https://api.yelp.com/v3/businesses/search"
params = {
    'term': 'bookstore',
    'location': 'San Francisco'
}
header = {'Authorization': 'Bearer {}'.format(api_key)}

# Get data about NYC cafes from the Yelp API
response = requests.get(base_url=api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data['businesses'])

# View the data's dtypes
print(cafes.dtypes)



# Create dictionary to query API for cafes in NYC
parameters = {'term': 'cafe',
          	  'location': 'NYC'}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                params=parameters,
                headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data['businesses'])
print(cafes.head())



# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(
    api_url,
    headers=headers,
    params=params
)



# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data['businesses'])
print(cafes.name)



# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep='_')

# View data
print(cafes.head())




# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=["name", 
                                  "alias",  
                                  "rating",
                          		  ["coordinates","latitude"], 
                          		  ["coordinates", "longitude"]],
                    		meta_prefix="biz_")


# View the data
print(flat_cafes.head())



# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset":50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)




# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(
    crosswalk,
    left_on='location_zip_code',
    right_on='zipcode'
)



# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(
    pop_data,
    left_on='puma',
    right_on='puma'
)

# View the data
print(cafes_with_pop.head())