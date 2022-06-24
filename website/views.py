from flask import Blueprint, redirect,render_template,request,flash
from flask_login import login_required,current_user
from .models import Note, Preferences
from .models import Biblio, User
from . import db
from .script import *
from scipy.spatial import distance
from sqlalchemy import create_engine, Column, Integer, String, text


engine = create_engine('sqlite://', echo=False)


views=Blueprint('views',__name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    
      
       return render_template('home.html',user=current_user)

@views.route('/index',methods=['POST','GET'])
@login_required
def index():
   #Biblio.__table__.drop(engine)
   #User.__table__.drop(engine)
   return render_template('index.html',user=current_user,biblios=dataBiblio)

@views.route('/emprunt',methods=['POST','GET'])
@login_required
def emprunt():

    

    if request.method=='POST': 
        
          #type=request.form.get('type')
          categorie=request.form.get('categorie')
          #note=int(request.form.get('note'))
          #titre=request.form.get('titre')
          new_biblio=Biblio(categorie=categorie,user_id=current_user.id)
          db.session.add(new_biblio)
          db.session.commit()
          flash('Biblio ajoutée avec succés',category='success')
   
    return render_template('emprunt.html',user=current_user,biblios=dataBiblio)


@views.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return 'The URL /predict is accessed directly. Go to the main page firstly'

    if request.method == 'POST':
        categorie=request.form.get('categorie_statistique_1')
        langue=request.form.get('langue')
          #note=int(request.form.get('note'))
          #titre=request.form.get('titre')
        #Biblio.query.delete()
        new_pref=Preferences(categorie=categorie,langue=langue,user_id=current_user.id)
        db.session.add(new_pref)
        db.session.commit()
        flash('Biblio ajoutée avec succés',category='success')

        input_val = request.form

        if input_val != None:
            # collecting values
            vals = []
            for key, value in input_val.items():

               if(value == "francais"):
                  value=1
               if(value == "anglais"):
                  value=0
               
               print("La clée ", key , " la valeur ",value)
               vals.append(float(value))

        # Calculate Euclidean distances to freezed centroids
        with open('model.pkl', 'rb') as file:
            freezed_centroids = pickle.load(file)

        assigned_clusters = []
        l = []  # list of distances

        for i, this_segment in enumerate(freezed_centroids):
            print(this_segment)
            dist = distance.euclidean(*vals, this_segment)
            print(dist)
            l.append(dist)
            index_min = np.argmin(l)
            assigned_clusters.append(index_min)

        
        clusters = pd.read_json('D:/Users/msellami2/Desktop/Projet M2/SmartLoan/dta_Biblio.json')
        df = pd.DataFrame(clusters,columns=['langue','titre','date','nombre_de_pret_total','categorie_statistique_1','cluster','note'])
        
        class livre: 
            def __init__(self, langue, titre,date,nombre_de_pret_total,categorie_statistique_1,cluster,note): 
               self.langue = langue 
               self.titre = titre
               self.date = date
               self.nombre_de_pret_total = nombre_de_pret_total
               self.categorie_statistique_1 = categorie_statistique_1
               self.cluster = cluster
               self.note=note
        dataFrameFinal=[]
        for index,row in df.iterrows():
          
            if(row['cluster']==index_min):
               #print(row['cluster'])
               print(index)
               dataFrameFinal.append( livre(row['langue'] ,row['titre'] ,row['date'],row['nombre_de_pret_total'] ,row['categorie_statistique_1'] ,row['cluster'] ,row['note']    ))
               #print(dataFrameFinal)
            #    print(row[cluster])    
       
        print("TAILLE DE LA LISTE ",len(dataFrameFinal))
        print('*********************les clusters defoooooo*****************************')      

        for i in dataFrameFinal:
            print(i)  
        

        flash(f'Vous faites partie du cluster {index_min}',category='success')

        return render_template(
            'predict.html',user=current_user,datafr=dataFrameFinal, result_value=f'Segment = #{index_min}'
            )
@views.route('/delete/<int:id>')
def deleteById(id):
    p = Preferences.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()

    
    return redirect("/")



   