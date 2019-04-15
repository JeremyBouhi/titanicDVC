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
-f : the file name where the step will be described (if -f not specified the file will be named after the output file, i.e 'model.p.dvc', if there is no -o option, it will be called Dvcfile)
-d : for the dependencies 

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

###Create pipeline
    dvc run -f prepare.dvc -d src/prepare.py -d data/train.csv python src/prepare.py
We don't need to do :
    
    dvc add prepare.dvc
because when you do 'dvc run', it automatically saves it in the cache and takes the file under DVC control

    dvc run -d src/train.py -d data/matrix-train.p -o data/model.p -f train.dvc python src/train.py
    dvc run -f evaluate.dvc -d src/evaluate.py -d data/model.p -m data/eval.txt python src/evaluate.py 