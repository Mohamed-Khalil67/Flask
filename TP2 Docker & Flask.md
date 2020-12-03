## Cheat Sheet  

**1.1- Docker & Flask **

- comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
- installer docker sur votre machine (Ubuntu de préférence, si pas de machine ubuntu vous pouvez faire un double boot ou bien installer une VM en profitant de l'accès gratuit d'un éditeur cloud GCP, Azur, AWS...) 
- lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
  - docker run hello-world command , is working succeefully.
- regarder si votre container est bien lancer 
  - on vérifie avec docker ps -a , pour voire tout les containers
- Un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers :-
  - Les commandes docker `build`, `run` et `exec` :
    - Build : " docker build -t python-miniapp:01 . " on construrire l'image avec la commande docker build de marquer cette image d'un certain tag  avec l'option -t - le . signifie que la commande devra se servir du dossier courant pour construire l'image python-miniapp:01 de tagé 01
    - Run : commandes à executer pour construire .l'application, ici l'installation de pip qui va nous servir à importer ce dont notre application à besoin
    - Exec :
  - Pour ne pas utiliser sudo à chaque fois :
    - sudo groupadd docker
    - sudo gpasswd -a $USER docker
  - Les commandes générales importantes :
    - sudo docker build -t python-miniapp:01 .
    - sudo docker run -d -p 5000:5000 python-miniapp:01
    - docker exec -it "container ID" /bin/bash
    - docker logs "CONTAINER ID" #status of the container
    - docker stop "CONTAINER ID"
    - docker start "CONTAINER ID"
    - docker ps #tous les container actives
    - docker ps -a #tous les containers actives et non actives  
    - sudo docker system prune -a && sudo docker images purge # Delete all images and containers
  - expliquer ce qu'est un port dans un container
    - port : un port permet de mapper le port local avec le port virtuel
    - Utilité du requirements.txt : le requirements.txt permet de récupérer la liste des paquets installées
- How to create Virtualenv on Ubuntu : (important to install certain packages)
  - Install virtualenv package
    - pip install virtualenv
  - Create the virtual enviroment
    - virtualenv mypython
  - Activate the virtual enviroment
    - source mypython/bin/activate ( Ubuntu )
    - mypython\Scripts\activate ( Windows )
  - Deactivate the virtual enviroment
    - deactivate

**1.2- Project Heroku_Flask_Docker  **

- Build the Docker image locally and run to make sure that the service is running :

  - ```
    docker build -t flask-heroku:latest .
    docker run -d -p 5000:5000 flask-heroku
    ```

- Opening the localhost on port 5000 should open our output :

  - http://0.0.0.0:5000

- Deploying the application to Heroku :-

  - heroku container:login
  - heroku create bookapp67 
    - Les 3 fichiers les plus importants book.py , requirements.txt et Dockerfile.
  - heroku container:push web --app bookapp67
    - To create the container onto Heroku
  - heroku container:release web --app bookapp67

- Mettre à jour l'api :

  - les mêmes étapes avec une changement de tag
    - Alors , bookapp67.01 et bookapp67.02
