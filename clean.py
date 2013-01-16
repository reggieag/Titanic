import csv
import pandas as pd
import numpy as np

cd D:\Kaggle\Titantic
data = pd.read_csv('train.csv')

#drop name column since cant really turn into floats
data = data.drop('name', axis = 1)
#replace female with 1 and male with 0
data['sex'] = data['sex'].replace('female',1)
data['sex'] = data['sex'].replace('male',0)
#set missing ages to mean of ages
data['age'] = data['age'].fillna(data['age'].mean())

