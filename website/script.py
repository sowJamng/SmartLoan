import pandas as pd
import random
import numpy as np
from sklearn import metrics
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn import model_selection
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn import preprocessing
import json
from sklearn.preprocessing import StandardScaler

def display(donnees):
   print("Dimensions des données : " + str(donnees.shape))
   print(donnees.dtypes)
  # print(donnees.isnull().sum())
  # print(donnees.head(10))

def import_data(l):
  cols = [x for x in range (37)]
  donnees = pd.read_csv('D:/Users/msellami2/Biblio.csv', usecols=cols,sep=";" , low_memory=False)
  donnees.drop(['isbn','issn','ean','edition','ndeg','co_auteur_nom','co_auteur_prenom' ,'dates', 'auteur_secondaire_nom', 'auteur_secondaire_prenom',
  'auteur_secondaire_dates', 'auteur_collectivite', 'subdivision_auteur_collectivite', 'co_auteur_collectivite', 'subdivision_co_auteur_collectivite',
  'auteur_secondaire_collectivite', 'subdivision_auteur_secondaire_collectivite', 'cote_majoritaire',
  'nombre_de_localisations', 'titre_de_serie', 'auteur_nom', 'auteur_prenom', 'auteur_dates', 'indice', 'nombre_de_prets_2017', 'collection',
  'nombre_d_exemplaires', 'format', 'editeur', 'nombre_de_pret_annee_2018_au_26_juillet_2018'], axis=1,inplace=True)
  donnees.drop(donnees.tail(l).index,inplace=True)
 
  #print(donnees.shape)
  return(donnees)

def replace_null(donnees):
  donnees['nombre_de_pret_total'].fillna(0.0, inplace=True)
  donnees=donnees.fillna("0", inplace=True)
  donnees=pd.DataFrame(donnees)
  # print(donnees.shape)
  

def generate_data(donnees):

  pd.set_option("mode.chained_assignment", None)
  mylist = []
  donnees=pd.DataFrame(donnees)
  for i in range(0,100):
    x = random.randint(1,45)
    mylist.append(x)
  for row in range(1534):
    #donnees['Utilisateur']="Utilisateur"
    donnees=donnees.assign(Profil='auteur') 
    
  for row in range(1534):
    num=random.choice(mylist)
    #donnees['Utilisateur'][row]="Utilisateur"+str(num)
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

  return(donnees)

def separate_data(donnees):
  donneesNp=donnees.to_numpy()
  x = donneesNp[:,2:9:]
  y = donneesNp[:,9:10]
  #print(x.shape, y.shape)
  x_normalized=preprocessing.StandardScaler().fit_transform(x)
  x_train,x_test,y_train,y_test = model_selection.train_test_split(x_normalized,y,test_size = 0.8)
  # print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
  # print(pd.DataFrame(x_train).head())
  kmeans = cluster.KMeans(n_clusters=4)
  kmeans.fit(x_train)
  labels=kmeans.predict(x_train)
  # print(y_train)
  # print(labels)

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
  replace_null(emprunt)
  emprunt=generate_data(emprunt)
  # emprunt=transform_data(emprunt)
  #display(emprunt)
  # separate_data(emprunt)
  #print(emprunt)
  return emprunt

dataBiblio=main_script()
data=generateUser(dataBiblio)

Encoder =preprocessing.LabelEncoder()
data["langue"]=Encoder.fit_transform(data["langue"] )
data["titre"]=Encoder.fit_transform(data["titre"])
data["date"]=Encoder.fit_transform(data["date"] )
data["libelle_v_smart_et_webopac"]=Encoder.fit_transform(data["libelle_v_smart_et_webopac"] )
data["categorie_statistique_1"]=Encoder.fit_transform(data["categorie_statistique_1"])
data["Profil"]=Encoder.fit_transform(data["Profil"])
data["date"]=Encoder.fit_transform(data["date"])
data["Email"]=Encoder.fit_transform(data["Email"])
data["Prenom"]=Encoder.fit_transform(data["Prenom"])
data["Nom"]=Encoder.fit_transform(data["Nom"])
data["Password"]=Encoder.fit_transform(data["Password"])

kmeans = KMeans(n_clusters = 4)
kmeans.fit(data)
labels = kmeans.predict(data)
centres = kmeans.cluster_centers_
#data = data.set_index('id', drop = False)
for row in range(1534):
   data['cluster']="cluster"
for row in range(1534):
   data['cluster'][row]=labels[row]
       
#df=pd.DataFrame({'user_id':data.index,'cluster':labels})

# df = pd.DataFrame({'user_id':data.index,
#                    'langue':data['langue'],
#                    'titre':data['titre'],
#                    'Email':data['Email'],
#                    #'Prenom':data['Prenom'],
#                    #'Nom':data['Nom'],
#                   # 'Password':data['Password'],
#                    'libelle_v_smart_et_webopac':data['libelle_v_smart_et_webopac'],
#                    'nombre_de_pret_total':data['nombre_de_pret_total'],
#                    'Note':data['Note'],
#                    'categorie_statistique_1':data['categorie_statistique_1'],
#                    'labels':labels}).sort_values(by=['user_id'],axis = 0)
#print(df)
# Convertir le dataframe en json 
df_json = data.to_json(path_or_buf='dta_Biblio.json',orient="records")
#parsed = json.loads(datajson)
#json.dumps(parsed,indent=4)

print(df_json)
