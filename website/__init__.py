from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .script import *

db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] ='smartLoanNanterre'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
        
    from .views import views
    from .auth import auth
    
   # app.register_blueprint(views,urlprefix='/')
    app.register_blueprint(auth,urlprefix='/')
    app.register_blueprint(views,urlprefix='/index')

    from .models import User
    create_databases(app)
    
    login_manager=LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    return app


def create_databases(app):
    if not path.exists(DB_NAME):
        db.create_all(app=app)
        from .models import Cluster
        from .models import User
       # if db.session.query(Cluster.query.filter(Cluster.id == 1).exists()).scalar()==False:
        u= User.query.all()
        c=Cluster.query.all()
        cluster0=Cluster(numcluster="0")
        cluster1=Cluster(numcluster="1")
        cluster2=Cluster(numcluster="2")
        cluster3=Cluster(numcluster="3")
        db.session.add(cluster0)
        db.session.add(cluster1)
        db.session.add(cluster2)
        db.session.add(cluster3)
        db.session.commit()
        users = pd.read_json('C:/Miage/ML/projet/SmartLoan/biblio_user.json')
        df = pd.DataFrame(users,columns=['Prenom','Email','Password','cluster'])
        for index,row in df.iterrows():
            # if not User.query.filter_by(email=row['Email']).first():
                #cluster= Cluster.query.filter_by(cluster=row['cluster']).first()
                new_user=User(email=row['Email'],prenom= row['Prenom'],password=generate_password_hash(row['Password'][row],method='sha256'),clusters=row['cluster'])
                db.session.add(new_user)
                db.session.commit()
        