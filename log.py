#Logistic Regression Implementation

import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
outputCSV = raw_input('What do you want to name the csv? ') + '.csv'

def clean_data(Data_Frame):
#drop name column since cant really turn into floats
	Data_Frame = Data_Frame.drop(['name','cabin','ticket','embarked','parch'], axis = 1)
#replace female with 1 and male with 0
	Data_Frame['sex'] = Data_Frame['sex'].replace(['male','female'],[0,1])
#set missing ages to mean of ages
	Data_Frame['age'] = Data_Frame['age'].fillna(Data_Frame['age'].mean())
	Data_Frame['fare'] = Data_Frame['fare'].fillna(Data_Frame['fare'].mean())
	return Data_Frame
	
train_data = clean_data(train_data)
test_data = clean_data(test_data)

Log_Reg = LogisticRegression()
Log_Reg = Log_Reg.fit(train_data.ix[:,"pclass":],train_data.ix[:,"survived"])

Output = Log_Reg.predict(test_data)
np.savetxt(outputCSV,Output)
