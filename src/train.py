from sklearn.ensemble import RandomForestRegressor
import conf
import pickle

train_matrix = conf.train_matrix
labels = conf.labels

output = conf.model

with open(train_matrix, 'rb') as fd:
    X = pickle.load(fd)

with open(labels, 'rb') as fd:
    y = pickle.load(fd)

forest = RandomForestRegressor()
forest.fit(X, y)

print(forest)

with open(output, 'wb') as fd:
    pickle.dump(forest, fd)