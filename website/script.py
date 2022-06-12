import pandas as pd
import random
import numpy as np
from sklearn import metrics
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn import model_selection
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import preprocessing
import json
from sklearn.preprocessing import StandardScaler
import pickle

def display(donnees):
   print("Dimensions des données : " + str(donnees.shape))
   print(donnees.dtypes)

def import_data(l):
  cols = [x for x in range (37)]
  donnees = pd.read_csv('D:/Users/msellami2/Biblio.csv', usecols=cols,sep=";" , low_memory=False)
  donnees.drop(['isbn','issn','ean','edition','ndeg','co_auteur_nom','co_auteur_prenom' ,'dates', 'auteur_secondaire_nom', 'auteur_secondaire_prenom',
  'auteur_secondaire_dates', 'auteur_collectivite', 'subdivision_auteur_collectivite', 'co_auteur_collectivite', 'subdivision_co_auteur_collectivite',
  'auteur_secondaire_collectivite', 'subdivision_auteur_secondaire_collectivite', 'cote_majoritaire',
  'nombre_de_localisations', 'titre_de_serie', 'auteur_nom', 'auteur_prenom', 'auteur_dates', 'indice', 'nombre_de_prets_2017', 'collection',
   'format', 'editeur', 'ndeg_de_notice','nombre_de_pret_annee_2018_au_26_juillet_2018','libelle_v_smart_et_webopac','nombre_d_exemplaires'], axis=1,inplace=True)
  
  return(donnees)



def generate_data(donnees):
    dataFr=donnees[(donnees['langue'] =='français')]
    dataEn=donnees[(donnees['langue']=='anglais')]
    print(donnees.shape)
    donnees=pd.concat([dataFr,dataEn])
    print(donnees.shape)
    donnees['categorie_statistique_1'].unique()
    cat1=donnees[(donnees['categorie_statistique_1'] =='D002 Informatique et ordinateurs')]
    cat2=donnees[(donnees['categorie_statistique_1']=='D103 Psychologie')] 
    cat3=donnees[(donnees['categorie_statistique_1'] == 'D901 Histoire generale')]
    cat4=donnees[(donnees['categorie_statistique_1']=='D711 Sport')]
    cat6=donnees[(donnees['categorie_statistique_1']=='D602 Medecine et sexualite')]
    cat7=donnees[(donnees['categorie_statistique_1'] =='D607 Gestion')]
    cat8=donnees[(donnees['categorie_statistique_1']=='D708 Cinema')]
    cat9=donnees[(donnees['categorie_statistique_1'] =='D910 Geographie')]
    cat10=donnees[(donnees['categorie_statistique_1']== 'D305 Droit, administration, questions sociales')]
    cat11=donnees[(donnees['categorie_statistique_1'] =='D801 Etudes litteraires, revues litteraires')]
    cat12=donnees[(donnees['categorie_statistique_1']== 'D101 Philosophie')]
    cat13=donnees[(donnees['categorie_statistique_1'] =='D502 Math., astronomie, physique, chimie')]
    cat14=donnees[(donnees['categorie_statistique_1']=='D303 Economie sauf metiers, commerce')]

    print(donnees.shape)
    donnees=pd.concat([cat1,cat2,cat3,cat4,cat6,cat7,cat8,cat9,cat10,cat12,cat13,cat14])
    nombprt=donnees[(donnees['nombre_de_pret_total']<5)]
    donnees=pd.concat([nombprt])
    print(donnees.shape)
    
    return(donnees)


def clustering(donnees):
  
   Encoder =preprocessing.LabelEncoder()
   donnees=donnees.dropna(axis = 0, how ='any')
   data=donnees[['langue','categorie_statistique_1','nombre_de_pret_total']]
   #data=data.dropna(axis = 0, how ='any')
   #donnees=donnees.dropna(axis = 0, how ='any')
   data["langue"]=Encoder.fit_transform(data["langue"] )
   data["categorie_statistique_1"]=Encoder.fit_transform(data["categorie_statistique_1"])
   #data["nombre_de_pret_total"]=Encoder.fit_transform(data["nombre_de_pret_total"])
   X = data
   print('taille X')
   print(X.shape) 
   model = KMeans(n_clusters=3, random_state=130)
   # fit the model
   model.fit(X)
   # predict the values
   y_predicted = model.fit_predict(X)
   print(y_predicted)
   print(X)
   # add the new column to the dataframe
   donnees['cluster'] = y_predicted
   data['cluster']=y_predicted
   # display the dataframe
   print(donnees.shape)
   # check the number of clusters
   donnees['cluster'].unique()
   # change the data type
   donnees = donnees['cluster'].astype(object)
   # serializing our model to a file called model.pkl
   pickle.dump(model, open("model.pkl","wb"))
   
   return donnees

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
 
def main_script():
  emprunt=import_data(814000)
  
  emprunt=generate_data(emprunt)
  emprunt=clustering(emprunt)
  display(emprunt)

  return emprunt

dataBiblio=main_script()
data=generateUser(dataBiblio)

