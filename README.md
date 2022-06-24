# Flask backend API AND FRONTEND 
# Que faisons nous ?
SmartLoad est une application utilisable par tous qui permet de proposer des livres au utilisateur en fonction de leurs preferences 

# Installation
## Prérequis
  
* [Télécharger Git](https://git-scm.com/downloads)
* [Télécharger Python 3.9](https://www.python.org/downloads/release/python-390/)
* [Installer Docker](https://www.docker.com/get-started)
  
## Démarrage
* Cloner le repository  
* Lancer le docker
* Lancer le projet
* Installer les dépendances
* Lancer le script de création de données: `python main.js`

`git clone https://github.com/sowJamng/SmartLoan.git`
`mkdir backend`
`python -m venv .\venv`
`.\ven\Scripts\activate`
`pip install flask`
`pip install flask-pytest`
`pip install scikit-learn`
`python3 -m pip install -r requirements.txt`

 
Run `python amin.py` to start development server on port `8081` to watch files and restart on update.

## Use from docker container

Clone project on your remote machine (needs to have docker daemon installed), then build image (`docker build -t flask-backend .`) and finally run the image by using `docker run -p 8081:8081 -v /HOST/PATH/TO/BACKEND/FOLDER:/app flask-backend`.

# Diagramme De Sequence


![](doc/predict.svg)
# Auteurs
* **Maodo laba SOW** - [Github](https://github.com/sowJamng)   -   [LinkedIn](https://fr.linkedin.com/in/maodo-laba-sow-668244184/)
* **Mehdi Sellami**  - [Github](https://github.com/mehdisellami/) - [LinkedIn](https://fr.linkedin.com/in/mehdisellami/)

**copiright: 2021/2022**