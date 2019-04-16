import conf
import pickle
from sklearn.metrics import accuracy_score

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

with open(conf.X_test, 'rb') as fd:
    X_test = pickle.load(fd)

with open(conf.y_test, 'rb') as fd:
    y_test = pickle.load(fd)

#%%
auc = model.score(X_test, y_test)

#%%
print(auc)

#%%

with open(conf.metrics, 'w') as fd:
    fd.write('AUC: {:4f}\n'.format(auc))