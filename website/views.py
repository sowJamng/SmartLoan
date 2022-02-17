from flask import Blueprint,render_template,request,flash
from flask_login import login_required,current_user
from .models import Note
from .models import Biblio
from . import db

views=Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
       if request.method=='POST': 
          type=request.form.get('type')
          categorie=request.form.get('categorie')
          note=request.form.get('note')
          new_biblio=Biblio(type=type,categorie=categorie,note=note,user_id=current_user.id)        
          db.session.add(new_biblio)
          db.session.commit()
          flash('Biblio ajoutée avec succés',category='success')
       
       return render_template('home.html',user=current_user)

@views.route('/index',methods=['POST','GET'])
def index():
   return render_template('index.html',user=current_user)