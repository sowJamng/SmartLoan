# Importation des biblithèques nécessaires
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import metrics
import json
from .script import  main_script
# Importer les donnees fakeUsers depuis l'api laravel

#url = "users_json_datacfrom_laravel.json"
#data = pd.read_json(url)
data= main_script()
# Remplacer l'index du dataframe par l'id du user
data = data.set_index('id', drop = False)
'''
print(data)
'''

#Labellisation des champ textes avec Encoder
Encoder =preprocessing.LabelEncoder()
data["ville"]=Encoder.fit_transform(data["ville"])


#création d'un clusetr Kmeans avec nombre de clusters 4
kmeans = KMeans(n_clusters = 4)
#Apprentissage fonction fit)
kmeans.fit(data)
#Prédiction et enregistrement des labels 
labels = kmeans.predict(data)
#Affichage des labels
'''
print('labels:')
print(labels)
'''
#enregistrement des centres des clusters
centres = kmeans.cluster_centers_
#Affichage des centres
'''
print('centres:')
print(centres)
'''
#Calculer le score du modèle
kmean_score= metrics.silhouette_score(data,labels)

print('score : %f' %kmean_score)


# Créer un dataframe pour stocker les labels des clusters et les noms des utilisateurs
df = pd.DataFrame({'user_id':data['id'],'labels':labels}).sort_values(by=['user_id'],axis = 0)

print(df)

# Convertir le dataframe en json 
datajson = df.to_json(orient="records")
parsed = json.loads(datajson)
json.dumps(parsed,indent=4)



print(datajson)