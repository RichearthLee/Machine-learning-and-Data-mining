import pandas as pd
import numpy as np

data = pd.read_csv(r'C:/Users/heave/Project/titanic_data.csv')
data["Age"] = data["Age"].fillna(data["Age"].median())#print(data)

#print(data.info())
print(data.head())
#print(data.describe())



