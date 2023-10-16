# Working with Pandas
geography = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd

brics = pd.DataFrame(geography)
print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

cars = pd.read_csv('./test-data/cars.csv')
print(cars)

# outputs a Pandas Series
print(cars['make'])

# outputs a Pandas DataFrame
print(cars[['make']])

# outputs data from index given
print(cars.iloc[2])

# outputs data for given labels (seemingly numeric if index is numeric)
print(cars.loc[[0]])
