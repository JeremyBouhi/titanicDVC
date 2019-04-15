from sklearn.tree import DecisionTreeRegressor
import conf
import pickle

train_matrix = conf.train_matrix
labels = conf.labels

output = conf.model

with open(train_matrix, 'rb') as fd:
    X = pickle.load(fd)

with open(labels, 'rb') as fd:
    y = pickle.load(fd)

treereg = DecisionTreeRegressor()
treereg.fit(X, y)

print(treereg)

with open(output, 'wb') as fd:
    pickle.dump(treereg, fd)