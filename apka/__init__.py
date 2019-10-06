# init.py

from flask import Flask, session
import pyrebase
import os
import stripe

# firebase login management
config = {
    "apiKey": "AIzaSyDoPJa0ZEfmJAHSjhes4fs_IYl-iCdZ9no",
    "authDomain": "mmgb-71d7c.firebaseapp.com",
    "databaseURL": "https://mmgb-71d7c.firebaseio.com",
    "projectId": "mmgb-71d7c",
    "storageBucket": "",
#    "messagingSenderId": "1074733389368",
#    "appId": "1:1074733389368:web:3e18f1312cb3413a0238cd",
#    "measurementId": "G-3X4W23EJ68"
    }

# setting up stripe test environment
STRIPE_PUBLISHABLE_KEY = 'pk_test_omDHnDeOVnBm3GP5X55ClS4S00Q4BzfbI1'  
STRIPE_SECRET_KEY = 'sk_test_sXIujAf7GCL5fKCT7X8xgS5t00U1i6gj1J'

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

 