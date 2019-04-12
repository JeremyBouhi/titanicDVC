import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv("../data/train.csv")

def isFemaleOrNot(str) :
    if (str == 'female'):
        return 1
    else:
        return 0

df['Preds']= df.apply(lambda x: isFemaleOrNot(x['Sex']), axis=1)

print(df[['Preds', 'Sex']])

# Evaluate accuracy
print(accuracy_score(df['Survived'], df['Preds']))
