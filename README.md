#How to use DVC

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
We describe each step of the pipeline
-f : the file name where the step will be described
-d : for the dependencies 
<cmd> : what to do

    dvc run -f main.dvc -d src/main.py -d data/train.csv python src/main.py

Il est important de spécifier les dépendances puisque c'est comme cela que DVC peut savoir si les fichiers nécessaires à l'étape ont été modifié (si aucune dépendance n'est spécifiée, c'est comme si tous les fichiers sont nécessaires à l'étape donc tous seront recompilés)

On peut ensuite push sur le repo dvc la description de la pipeline (main.dvc) pour qu'elle puisse être rejouée par d'autres collaborateurs

    git add main.dvc
    git commit -m 'add the training of the model to the pipeline'
    dvc push
    
###Visualize
    dvc pipeline show main.dvc
   
Use --ascii option for a better display

###Reproduce
    dvc repro main.dvc
    
###Mesure
To tell DVC you want to use that file as metrics :
    
    dvc metrics add data/eval.txt

But to do that, you first need to re-write the step before because you need to mention data/eval.txt as an output file (-o option). You don't need to delete main.dvc, you can overwrite it :
    
    dvc run -f main.dvc -d src/main.py -d data/train.csv -o data/eval.txt python src/main.py
 
###Delete
To properly delete main.dvc you need to :

    dvc remove main.dvc -p

(-p option for purge)

###Experiment
When you change of branch, you need to get the right data folders. 

    git checkout using-linear-regression
    dvc checkout
    
Git tracks the 'evaluate.dvc' file, which has the 'model.p' file as a dependence. So you need to retrieve this file which is really easy using DVC