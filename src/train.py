from sklearn.ensemble import RandomForestRegressor
import conf
import pickle

output = conf.model

with open(conf.X_train, 'rb') as fd:
    X_train = pickle.load(fd)

with open(conf.y_train, 'rb') as fd:
    y_train = pickle.load(fd)

forest = RandomForestRegressor()
forest.fit(X_train, y_train)

print(forest)

with open(output, 'wb') as fd:
    pickle.dump(forest, fd)