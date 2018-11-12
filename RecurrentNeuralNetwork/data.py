#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np

data = pd.read_csv(r'C:/Users/heave/Project/titanic_data.csv')
data["Age"] = data["Age"].fillna(data["Age"].median())
#print(data)
#print(data.info())
#print (data["Sex"].unique())
print(data.head())
#print(data.describe())



# In[18]:


print (data["Sex"].unique())
data.loc[data["Sex"] == "male" , "Sex"]=0
data.loc[data["Sex"] == "female" , "Sex"]=1


# In[ ]:





# In[ ]:




