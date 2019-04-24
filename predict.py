from src.conf import model
import pickle
from src.prepare import preprocess_data
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

#data_sent = {
#    'PassengerId': 892,
#    'Pclass': 3,
#    'Name': 'Kelly, Mr. James',
#    'Sex': 'male',
#    'Age': 34.5,
#    'SibSp': 0,
#    'Parch': 0,
#    'Ticket': 330911,
#    'Fare': 7.8292,
#    'Cabin': '',
#    'Embarked': 'Q'
#}

@app.route("/")
def hello():
    return "Hello World"

@app.route("/predict", methods=['POST'])
def predict():
    with open(model, 'rb') as fd:
        model_matrix = pickle.load(fd)

#%%
    data_sent = request.json
    print("data_sent: ", data_sent)
    #columns = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    columns = data_sent.keys()
    df_sent = pd.DataFrame(data_sent, columns=columns, index=[1])
    print("df_sent: ", df_sent)
    X_sent = preprocess_data(df_sent)
    print("X_sent: ", X_sent)
    y_preds = model_matrix.predict(X_sent)
    print("y_preds: ", y_preds)
    response = {
        "prediction": y_preds[0]
    }
    return jsonify(response)
