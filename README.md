#Titanic

###Installation
pip install dvc

###Initialize
git init
dvc init
git commit

###Configure
dvc remote add -d myremote /tmp/dvc-storage
git commit .dvc/config -m "initialize DVC local remote"

###Add Files
dvc add data/* va créer test.csv.dvc, train.csv.dvc etc. et va mettre data/* dans .gitignore 

###Share data
dvc push
ls -R /tmp/dvc-storage

###Retrieve data from .dvc
dvc pull

###Connect code and data
dvc run...
