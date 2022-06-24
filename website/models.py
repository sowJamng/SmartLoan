from .__init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now() )
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))


class Cluster(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    numcluster=db.Column(db.String(10))
    #user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
   
    
class Biblio(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(80))
    note=db.Column(db.Integer)
    titre=db.Column(db.String(100))
    categorie=db.Column(db.String(80))
    langue=db.Column(db.String(80))

class Livre(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(80))
    note=db.Column(db.Integer)
    titre=db.Column(db.String(100))
    categorie=db.Column(db.String(80))
    langue=db.Column(db.String(80))

    
class Preferences(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    categorie=db.Column(db.String(80))
    langue=db.Column(db.String(80))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
       
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
   # profil=db.Column(db.String(100))
    prenom=db.Column(db.String(80))
    profil=db.Column(db.String(50))
    password=db.Column(db.String(150))
    notes=db.relationship('Note')
    preferences=db.relationship('Preferences')
    clusters=db.relationship('Cluster')