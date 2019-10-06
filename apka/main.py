# main.py

from flask import Blueprint, render_template,request, flash, Markup,session
import numpy as np
import pickle
from apka import *
from apka import app

main = Blueprint('main', __name__)

pkl_file = open('dict_cat', 'rb')
index_dict = pickle.load(pkl_file)

pkl_file = open('dict_airlines.pkl', 'rb')
dict_airlines = pickle.load(pkl_file)

pkl_file = open('dict_airports.pkl', 'rb')
dict_airports = pickle.load(pkl_file)

@main.route('/')
def index():
    return render_template('index.html', pub_key=STRIPE_PUBLISHABLE_KEY)

@main.route('/profile')
def profile():
    if session.get('logged_in'):
        return render_template('profile.html', name=session['username'])
    return render_template('index.html')

@main.route('/pay')
def pay():
    if session.get('logged_in'):
        return render_template('pay.html', pub_key=STRIPE_PUBLISHABLE_KEY)        
    return render_template('index.html')

@main.route('/checkout',  methods=['POST'])
def checkout():
    if session.get('logged_in'):
        customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])
    
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=100,
            currency='usd',
            description='Flight delay prediction'
        )
        return render_template('get_prediction.html')
    return render_template('index.html')


@main.route('/get_prediction')
def get_prediction():
    if session.get('logged_in'):
        return render_template('get_prediction.html')
    return render_template('index.html')
    
@main.route('/get_prediction', methods=['POST'])
def get_prediction_post():

    global txt_origin 
    global txt_origin
    global txt_destination
    global txt_airline
    global text_day
    global text_tofd
    global text_ssn
    global prediction  
    global new_inputs
    
    in_origin = request.form.get('sel_origin')    
    in_destination = request.form.get('sel_destination')  
    in_airline = request.form.get('sel_airline')   
    in_season = request.form.get('sel_season')
    in_day = request.form.get('sel_day') 
    in_tofd = request.form.get('sel_tofd')
    
    new_inputs = np.zeros(len(index_dict))
    try:
        new_inputs[index_dict['TimeOfDay']] = in_tofd
    except:
        pass        

    try:
        new_inputs[index_dict['dow_'+str(in_day)]] = 1
    except:
        pass        

    try:
        new_inputs[index_dict['ssn_'+str(in_season)]] = 1
    except:
        pass   

    try:
        new_inputs[index_dict['arl_'+str(in_airline)]] = 1
    except:
        pass                    

    try:
        new_inputs[index_dict['dst_'+str(in_destination)]] = 1
    except:
        pass 

    try:
        new_inputs[index_dict['org_'+str(in_origin)]] = 1
    except:
        pass 

    if int(in_day)==1:
                    text_day = "Monday"
    elif int(in_day)==2: 
                text_day = "Tuesday"
    elif int(in_day)==3: 
                text_day = "Wednesday"
    elif int(in_day)==4: 
                text_day = "Thursday"
    elif int(in_day)==5: 
                text_day = "Friday"
    elif int(in_day)==6:
                text_day = "Saturday"
    else:
                text_day = "Sunday"  
                    
    if (int(in_tofd))==0:
                text_tofd = "forenoon"
    else:  
                text_tofd = "afternoon"
    
    if (int(in_season))==1:
                text_ssn = "Winter";
    elif (int(in_season))==2:  
                text_ssn = "Spring";
    elif (int(in_season))==3:
                text_ssn = "Summer";
    else:  
                text_ssn = "Autumn";
                
    txt_origin=str(dict_airports.loc[dict_airports.cde_id==int(in_origin)].airport.item())  
    txt_destination=str(dict_airports.loc[dict_airports.cde_id==int(in_destination)].airport.item())
    txt_airline=str(dict_airlines.loc[dict_airlines.code_id==int(in_airline)].airport.item())

    pkl_file = open('logreg_flights.pkl', 'rb')
    logreg_model = pickle.load(pkl_file)
        
    prediction = logreg_model.predict_proba(new_inputs.reshape(1,-1))

    return render_template('prediction.html', txt_origin=txt_origin, txt_destination=txt_destination, txt_airline=txt_airline, text_ssn=text_ssn,  text_tofd=text_tofd,  text_day=text_day, prediction= str(float(prediction[:,1].round(4)*100))+'%')

@main.route('/prediction')
def prediction():
    if session.get('logged_in'):
        return render_template('prediction.html', txt_origin=txt_origin, txt_destination=txt_destination, txt_airline=txt_airline, text_ssn=text_ssn,  text_tofd=text_tofd,  text_day=text_day, prediction= str(float(prediction[:,1].round(4)*100))+'%')
    return render_template('index.html')