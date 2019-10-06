# auth.py

from . import auth
from flask import Blueprint, render_template, redirect, url_for, request, flash
import pandas as pd
from apka import *
from apka import app

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if session.get('logged_in'):
        flash('You are logged in.') 
        return render_template('profile.html')
    else:        
        return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    try:
        user = authF.sign_in_with_email_and_password(email, password)
        session['logged_in']=True
        session['username'] = email

    except:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 

    return redirect(url_for('main.index'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        authF.create_user_with_email_and_password(email, password)
    except:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('main.index'))