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

#@app.route("/predict")
#def predict():
    # return y_preds

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

#%%
print(X_sent.shape)
print(X_sent)

y_preds = model.predict(X_sent)
print(y_preds)
print(y_preds.round())

#%%

#print(y_preds.round())

