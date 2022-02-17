from flask import Blueprint,render_template,flash,request,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('login avec succes ',category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))
            else:
               flash('Mot de passe incorrecte',category='error')
        else:
            flash('l email fournit est invalide,veuillez réessayer',category='error')       
    return render_template('login.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
     logout_user()
     return redirect(url_for('auth.login'))
 
 
@auth.route('/sign-up',methods=['POST','GET'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        prenom=request.form.get('prenom')
        profil="Profil A"
        pass1=request.form.get('password')
        pass2=request.form.get('cpassword') 
        
        user=User.query.filter_by(email=email).first()
        if user:
            flash('l\'adresse email fournit existe déjà')
        elif len(email) <4:
            flash('L\'Adresse email fournit doit etre superieur à 4 caracteres',category='error')
        
        elif len(password1)<7:
            flash('Le mot de passe doit etre suprieur à 7 careactere ',category='error')
        elif pass1!=pass2:
            flash('Le mot de posse ne correepond pas',category='error')
        else:
            new_user=User(email=email,prenom=prenom,password=generate_password_hash(pass1,method='sha256'),profil=profil)
            db.session.add(new_user)
            db.session.commit()
            login_user(user,remember=True)
            flash('Compte crée avec succés',category='success')
            
            return redirect(url_for('views.home'))
        
    return render_template('sign_up.html',user=current_user)
