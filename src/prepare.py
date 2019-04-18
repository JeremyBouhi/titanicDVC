import pickle

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

import conf

df = pd.read_csv("data/train.csv")

df_without_columns = df.drop(["Name", "Ticket", "Cabin", "Embarked", "PassengerId"], axis=1)
df_binarized = pd.get_dummies(df_without_columns, columns=["Sex"])

#For Age
imputer = Imputer(strategy="median")
X = imputer.fit_transform(df_binarized)
df = pd.DataFrame(X, columns=df_binarized.columns)

std = StandardScaler()
X = std.fit_transform(df)
df = pd.DataFrame(X, columns=df.columns)

print(df)

with open(conf.df, 'wb') as fd:
    pickle.dump(df, fd)
