import pandas as pd
import random
import numpy as np
from sklearn import metrics
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn import model_selection
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

def display(donnees):
  print("Dimensions des données : " + str(donnees.shape))
  print(donnees.dtypes)
  print(donnees.isnull().sum())
  print(donnees.head(10))

def import_data(l):
  cols = [x for x in range (37)]
  donnees = pd.read_csv('../Biblio.csv', usecols=cols,sep=";")
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

def generate_data(donnees):
  pd.set_option("mode.chained_assignment", None)
  mylist = []
  for i in range(0,100):
    x = random.randint(1,45)
    mylist.append(x)
  for row in range(1534):
    donnees['Utilisateur']="Utilisateur"
    donnees['Profil']='Profil'
  for row in range(1534):
    num=random.choice(mylist)
    donnees['Utilisateur'][row]="Utilisateur"+str(num)
    if num < 15 :
      donnees['Profil'][row]="Profil A"
    elif num < 30 :
      donnees['Profil'][row]="Profil B"
    elif num <= 45 :
      donnees['Profil'][row]="Profil C"
  tous = (donnees['Profil'] != '')
  a_aime = (donnees['Profil'] == 'Profil A') & ((donnees['categorie_statistique_1'] == 'LFRA Litterature francaise') | (donnees['categorie_statistique_1'] == 'D103 Psychologie'))
  a_aime_pas = (donnees['Profil'] == 'Profil A') & ((donnees['categorie_statistique_1'] == 'LBRI Litterature britannique') | (donnees['categorie_statistique_1'] == 'M310 Musique classique: 20eme et 21eme siecles'))
  b_aime = (donnees['Profil'] == 'Profil B') & ((donnees['categorie_statistique_1'] == 'LBRI Litterature britannique') | (donnees['categorie_statistique_1'] == 'D103 Psychologie'))
  b_aime_pas = (donnees['Profil'] == 'Profil B') & ((donnees['categorie_statistique_1'] == 'D602 Medecine et sexualite') | (donnees['categorie_statistique_1'] == 'LBDE Bandes dessinees'))
  c_aime = (donnees['Profil'] == 'Profil C') & (donnees['libelle_v_smart_et_webopac'] == 'Livre pour adulte')
  c_aime_pas = (donnees['Profil'] == 'Profil C') & (donnees['libelle_v_smart_et_webopac'] != 'Livre pour adulte')
  donnees.loc[tous,'Note'] = np.random.randint(6, size=sum(tous))
  donnees.loc[a_aime,'Note'] = np.random.randint(2, size=sum(a_aime))+4
  donnees.loc[a_aime_pas,'Note'] = np.random.randint(2, size=sum(a_aime_pas))
  donnees.loc[b_aime,'Note'] = np.random.randint(2, size=sum(b_aime))+4
  donnees.loc[b_aime_pas,'Note'] = np.random.randint(2, size=sum(b_aime_pas))
  donnees.loc[c_aime,'Note'] = np.random.randint(2, size=sum(c_aime))+4
  donnees.loc[c_aime_pas,'Note'] = np.random.randint(2, size=sum(c_aime_pas))

def transform_data(donnees):
  Encoder=preprocessing.LabelEncoder()
  donnees=donnees[["ndeg_de_notice","titre", "langue", "date", "libelle_v_smart_et_webopac","nombre_de_pret_total", "categorie_statistique_1", "Note", "Utilisateur", "Profil"]]
  donnees["langue"]=Encoder.fit_transform(donnees["langue"])
  donnees["titre"]=Encoder.fit_transform(donnees["titre"])
  donnees["date"]=Encoder.fit_transform(donnees["date"])
  donnees["libelle_v_smart_et_webopac"]=Encoder.fit_transform(donnees["libelle_v_smart_et_webopac"])
  donnees["nombre_de_pret_total"]=Encoder.fit_transform(donnees["nombre_de_pret_total"])
  donnees["categorie_statistique_1"]=Encoder.fit_transform(donnees["categorie_statistique_1"])
  donnees["Utilisateur"]=Encoder.fit_transform(donnees["Utilisateur"])
  donnees["Profil"]=Encoder.fit_transform(donnees["Profil"])
  donnees["Note"]=Encoder.fit_transform(donnees["Note"])
  return(donnees)

def separate_data(donnees):
  donneesNp=donnees.to_numpy()
  x = donneesNp[:,2:9:]
  y = donneesNp[:,9:10]
  print(x.shape, y.shape)
  x_normalized=preprocessing.StandardScaler().fit_transform(x)
  x_train,x_test,y_train,y_test = model_selection.train_test_split(x_normalized,y,test_size = 0.8)
  print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
  print(pd.DataFrame(x_train).head())
  kmeans = cluster.KMeans(n_clusters=3)
  kmeans.fit(x_train)
  labels=kmeans.predict(x_train)
  print(y_train)
  print(labels)

def main():
  emprunt=import_data(814000)
  replace_null(emprunt)
  generate_data(emprunt)
  emprunt=transform_data(emprunt)
  display(emprunt)
  #separate_data(emprunt)

if __name__ == "__main__":
    main()