import pickle

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

import conf

x = conf.train_matrix
Y = conf.labels

df = pd.read_csv("data/train.csv")
labels = df['Survived']

df_without_columns = df.drop(["Name", "Ticket", "Cabin", "Embarked", "PassengerId", "Survived"], axis=1)
data_binarized = pd.get_dummies(df_without_columns, columns=["Sex"])

imputer = Imputer(strategy="median")
X = imputer.fit_transform(data_binarized)
#reinject in pandas.Dataframe:
df = pd.DataFrame(X, columns=data_binarized.columns)

std = StandardScaler()
X = std.fit_transform(df)
df = pd.DataFrame(X, columns=df.columns)

print(df)

with open(x, 'wb') as fd:
    pickle.dump(df, fd)

with open(Y, 'wb') as fd:
    pickle.dump(labels, fd)