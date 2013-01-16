#Kaggle: Titantic - Random Forest
#This code cleans up the data for input into a simple Random Forest Algorithim 

import csv
import pandas as pd
import numpy as np

cd D:\Kaggle\Titantic
data = pd.read_csv('train.csv')

#drop name column since cant really turn into floats
data = data.drop(['name','cabin','ticket'] axis = 1)
#replace female with 1 and male with 0
data['sex'] = data['sex'].replace(['male','female'],[0,1])
#set missing ages to mean of ages
data['age'] = data['age'].fillna(data['age'].mean())

