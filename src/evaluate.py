import conf
import pickle
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.model_selection import cross_val_score

model = conf.model
train_matrix = conf.train_matrix
labels = conf.labels
metrics_file = conf.metrics

with open(model, 'rb') as fd:
    model = pickle.load(fd)
with open(train_matrix, 'rb') as fd:
    X = pickle.load(fd)
with open(labels, 'rb') as fd:
    y = pickle.load(fd)

linreg_score = cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=10)
linreg_rmse = np.sqrt(-linreg_score)

print(linreg_rmse)
print("Moyenne", linreg_rmse.mean())
print("Ecart-type", linreg_rmse.std())

with open(metrics_file, 'w') as fd:
    fd.write('RMSE: {:4f}\n'.format(linreg_rmse.mean()))