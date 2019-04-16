import os

data_dir = 'data'

train_matrix = os.path.join(data_dir, 'matrix-train.p')
labels = os.path.join(data_dir, 'labels.p')
model = os.path.join(data_dir, 'model.p')
metrics = os.path.join(data_dir, 'eval.txt')