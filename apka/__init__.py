# init.py

from flask import Flask, session
import pyrebase
import os
import stripe

# firebase login management
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
#    "messagingSenderId": "",
#    "appId": "",
#    "measurementId": ""
    }

# setting up stripe test environment
STRIPE_PUBLISHABLE_KEY = ''  
STRIPE_SECRET_KEY = ''

stripe.api_key = STRIPE_SECRET_KEY

txt_origin=''
txt_destination=''
txt_airline=''
text_day=''
text_tofd=''
text_ssn=''
prediction=0
new_inputs=0


#firebase
firebase = pyrebase.initialize_app(config)
#db = firebase.database()
authF = firebase.auth()
app = Flask(__name__, static_url_path='')

app.secret_key = os.urandom(12)


# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

 