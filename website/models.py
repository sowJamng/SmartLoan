from  . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now() )
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
   
    
class Biblio(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(80))
    date=db.Column(db.DateTime(timezone=True), default=func.now() )
    note=db.Column(db.Integer)
    categorie=db.Column(db.String(80))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    
       
class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    profil=db.Column(db.String(100))
    prenom=db.Column(db.String(80))
    password=db.Column(db.String(150))
    notes=db.relationship('Note')
    biblios=db.relationship('Biblio')