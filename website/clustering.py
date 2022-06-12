import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import rcParams and set the figure size
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5
from sklearn.cluster import KMeans

def import_data(l):
  cols = [x for x in range (37)]
  donnees = pd.read_csv('C:/Miage/ML/projet/Biblio.csv', usecols=cols,sep=";")
  donnees.head(10)
  donnees.drop(['isbn','issn','ean','edition','ndeg','co_auteur_nom','co_auteur_prenom' ,'dates', 'auteur_secondaire_nom', 'auteur_secondaire_prenom',
  'auteur_secondaire_dates', 'auteur_collectivite', 'subdivision_auteur_collectivite', 'co_auteur_collectivite', 'subdivision_co_auteur_collectivite',
  'auteur_secondaire_collectivite', 'subdivision_auteur_secondaire_collectivite', 'cote_majoritaire',
  'nombre_de_localisations', 'titre_de_serie', 'auteur_nom', 'auteur_prenom', 'auteur_dates', 'indice', 'nombre_de_prets_2017', 'collection',
  'nombre_d_exemplaires', 'format', 'editeur', 'nombre_de_pret_annee_2018_au_26_juillet_2018'], axis=1,inplace=True)
  donnees.drop(donnees.tail(l).index,inplace=True)
  return(donnees)

def replace_null(donnees):
  donnees['nombre_de_pret_total'].fillna(0.0, inplace=True)
  donnees=donnees.fillna("0", inplace=True)
  donnees=pd.DataFrame(donnees)
  print(donnees.shape)
  

def generateUser(data):
   mylist = []
   for i in range(0,400):
     x = random.randint(1,400)
     mylist.append(x)

   for row in range(15527):
      data['Email']="email"
      data['Prenom']="prenom"
      data['Nom']="name"
      data['Password']="password"

   for row in range(15527):
      num=random.choice(mylist)
      data['Prenom'][row]="Prenom"+str(num)
      data['Nom'][row]="Nom"+str(num)
      data['Email'][row]=str(num)+"@gmail.com"
      data['Password']="password"+str(num)
   return data  

def display(donnees):
      print("Dimensions des données : " + str(donnees.shape))
      print(donnees.head(10))
      
def main_script():
  emprunt=import_data(814000)
  replace_null(emprunt)
  emprunt=generateUser(emprunt)
  display(emprunt)
  replace_null(emprunt)
  return emprunt

dataBiblio=main_script()
