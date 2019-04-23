import pickle
import pandas as pd
import conf
import numpy as np


# %%

def grab_data():
    df = pd.read_csv("data/train.csv")
    return df

def clean_age(df):
    df['Age'].fillna(df['Age'].median(), inplace=True)
    bins = [0, 14, 25, 35, 60, np.inf]
    labels = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Senior']
    df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
    return df

def clean_family_size(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    bins = [0, 1, 2, 3, 4, np.inf]
    labels = ['0', '1', '2', '3', '>=4']
    df['FamilySize'] = pd.cut(df["FamilySize"], bins, labels=labels)
    return df

def preprocess_data(df):
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    df = clean_age(df)
    df = clean_family_size(df)
    print((df['FamilySize']==2).sum())
    drop_column = ['Fare', 'Name', 'Ticket', 'PassengerId', 'Parch', 'Cabin', 'SibSp', 'Parch', 'Age']
    df.drop(drop_column, axis=1, inplace=True)

    df = pd.get_dummies(df, columns=["AgeGroup", "Sex", "Embarked", "Pclass", "FamilySize"])
    return df

# %%
df_train = grab_data()
df_train = preprocess_data(df_train)
print((df_train.sum()))
#%%
with open(conf.df_train, 'wb') as fd:
    pickle.dump(df_train, fd)
