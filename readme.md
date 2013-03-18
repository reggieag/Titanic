Titanic Kaggle
===============
Walking through the Kaggle Titanic competition using the information found at this website:
http://inclass.kaggle.com/c/titanic-2012-for-stat-202/details/getting-started-with-random-forests

Data
----
train.csv - used to train the model.
test.csv - used to test the model.

myFirstRandomForest.py
----------------------
This implementation of random forest was done mostly by following the Kaggle instructions. This was more of an exercise of getting familiar with Kaggle and working with machine learning python packages.
A large portion of the code is using pandas to clean the data. This could have been easily done using a combination of excel and an EMAC, but as I mentioned before this project is more of a learning exercise than anything else.

feature_selection.py
----------------------
In this script I simplified the features to see if that would help the model. I drooped the embarked and parch columns and re-ran the random forest algorithm. I found that the model did improve.

logisticRegression.py
----------------------
Finally I ran a logistic regression model. At the time I was studying logistic regressions so it made sense to try and apply it in an actual project. I found that this model was not as accurate as the other two.
