import pickle

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

import conf

#%%
df_train = pd.read_csv("data/train.csv")
df_test = pd.read_csv("data/test.csv")

#%%
print(df_train)
#%%
print(df_train.isnull().sum())
#%% Filling the NaN values
df_train['Embarked'].fillna(df_train['Embarked'].mode()[0], inplace = True)
df_train['Fare'].fillna(df_train['Fare'].median(), inplace = True)
df_train['Age'].fillna(df_train['Age'].median(), inplace = True)

print('check the nan value in train data')
print(df_train.isnull().sum())
#%%
print(df_train.columns)

#%%

drop_column = ['Fare','Name','Ticket', 'PassengerId','Parch', 'Cabin']
df_train.drop(drop_column, axis=1, inplace = True)
#%%
df_train = pd.get_dummies(df_train, columns = ["Age","Sex","Embarked","Pclass", "SibSp"])
#%%
with open(conf.df_train, 'wb') as fd:
    pickle.dump(df_train, fd)
