from sklearn.ensemble import RandomForestClassifier
import conf
import pickle

train_matrix = conf.train_matrix
labels = conf.labels

output = conf.model

with open(train_matrix, 'rb') as fd:
    X = pickle.load(fd)

with open(labels, 'rb') as fd:
    y = pickle.load(fd)

rf = RandomForestClassifier(n_estimators=100, random_state=0, max_features=2)
rf.fit(X, y)

print(rf)

with open(output, 'wb') as fd:
    pickle.dump(rf, fd)