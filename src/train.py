from sklearn.linear_model import LinearRegression
import conf
import pickle

train_matrix = conf.train_matrix
labels = conf.labels

output = conf.model

with open(train_matrix, 'rb') as fd:
    X = pickle.load(fd)

with open(labels, 'rb') as fd:
    y = pickle.load(fd)

linreg = LinearRegression()
linreg.fit(X, y)

print(linreg)

with open(output, 'wb') as fd:
    pickle.dump(linreg, fd)