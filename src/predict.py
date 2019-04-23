import conf
import pickle
from prepare import preprocess_data
import pandas as pd
#from flask import Flask

#app = Flask(__name__)

data_sent = {
    'PassengerId': 892,
    'Pclass': 3,
    'Name': 'Kelly, Mr. James',
    'Sex': 'male',
    'Age': 34.5,
    'SibSp': 0,
    'Parch': 0,
    'Ticket': 330911,
    'Fare': 7.8292,
    'Cabin': '',
    'Embarked': 'Q'
}

columns = data_sent.keys()
print(columns)

#%%
df_sent = pd.DataFrame(data_sent, columns=columns, index = [1])
X_sent = preprocess_data(df_sent)

def add_missing_dummy_columns( d, columns ):
    missing_cols = set( columns ) - set( d.columns )
    for c in missing_cols:
        d[c] = 0

def fix_columns( d, columns ):

    add_missing_dummy_columns( d, columns )

    # make sure we have all the columns we need
    assert( set( columns ) - set( d.columns ) == set())

    extra_cols = set( d.columns ) - set( columns )
    if extra_cols:
        print("extra columns:", extra_cols)

    d = d[columns]
    return d



#@app.route("/predict")
#def predict():
    # return y_preds

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

#%%

X_sent = fix_columns(model, columns)
print(X_sent.shape)

print(X_sent)

y_preds = model.predict(X_sent)
print(y_preds)
#%%

#print(y_preds.round())

