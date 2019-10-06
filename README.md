# mlap_strup
## Midterm homework
### Team: Standalone 

### Application structure
1. Simple application for predicting flight delays based Kaggle competition dataset
2. Model calibration can be found in [notebook](https://github.com/GrzBoc/mlap_strup/blob/master/model_notebook/gb_HW05_def.ipynb)
3. Application operational model:
  - sing up is required to have access to flight delay functionality
  - then to be able to have a prediction an upfront payment has to be done with credit card
  - after payment prediction configuration panel is opend
4. Application configuration:
  - app is based on firebase auth engine, therefore to run it, configuration of config variable in __init__.py is required
  - payments are configured to Stripe test functionality and also require setting variable STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY in __init__.py file
 5. Application run in local environment by running gbaka.py with adress 127.0.0.1:4000



### Home screen
<p align="center"> <img src="/screenshots/01%20home.png" width="800"  height="480" ></p>

### Sign up screen
<p align="center"> <img src="/screenshots/02%20signup.png" width="800"  height="480" ></p>

### Login screen
<p align="center"> <img src="/screenshots/03%20login.png" width="800"  height="480" ></p>

### Home logged screen
<p align="center"> <img src="/screenshots/04%20home_logged.png" width="800"  height="480" ></p>

### Profile screen
<p align="center"> <img src="/screenshots/05%20profile.png" width="800"  height="480" ></p>

### Predict pay screen
<p align="center"> <img src="/screenshots/10%20predict_pay.png" width="800"  height="480" ></p>

### Predict payment screen
<p align="center"> <img src="/screenshots/11%20predict_payment.png" width="800"  height="480" ></p>

### Prediction setup screen
<p align="center"> <img src="/screenshots/11%20predict_setup.png" width="800"  height="480" ></p>

### Prediction result screen
<p align="center"> <img src="/screenshots/11%20predict_output.png" width="800"  height="480" ></p>
