import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/train.csv")
metrics_file = 'data/eval.txt'

def isFemaleOrNot(str) :
    if (str == 'female'):
        return 1
    else:
        return 0

df['Preds']= df.apply(lambda x: isFemaleOrNot(x['Sex']), axis=1)

print(df[['Preds', 'Sex']])

# Evaluate accuracy
auc =accuracy_score(df['Survived'], df['Preds'])

print(auc)

with open(metrics_file, 'w') as fd:
    fd.write('AUC: {:4f}\n'.format(auc))
