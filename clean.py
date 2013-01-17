#Kaggle: Titantic - Random Forest
#This code cleans up the data for input into a simple random forest algorithim. 
#It then implements the random forest algorithim on the cleaned up data. 

import csv
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

cd D:\Kaggle\Titantic
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

def clean_data(Data_Frame):
#drop name column since cant really turn into floats
	Data_Frame = Data_Frame.drop(['name','cabin','ticket'], axis = 1)
#replace female with 1 and male with 0
	Data_Frame['sex'] = Data_Frame['sex'].replace(['male','female'],[0,1])
#replace embarked with integers and fill the null values
	Data_Frame['embarked'] = Data_Frame['embarked'].replace(['S','C','Q'],[1,2,3])
	Data_Frame['embarked'] = Data_Frame['embarked'].fillna(0)
#set missing ages to mean of ages
	Data_Frame['age'] = Data_Frame['age'].fillna(Data_Frame['age'].mean())
	Data_Frame['fare'] = Data_Frame['fare'].fillna(Data_Frame['fare'].mean)
	return Data_Frame
	
train_data = clean_data(train_data)
test_data = clean_data(test_data)

Forest = RandomForestClassifier(n_estimators = 100)
Forest = Forest.fit(train_data,train_data
