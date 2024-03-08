# views.py
from django.shortcuts import render
from django.http import HttpResponse
import pickle
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from .models import LoanPrediction

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout



def home(request):
    return render(request, 'home.html')


def predict(request):
    return render(request, 'predict.html')



# ... (previous code)

# ... (previous code)

import pickle


def loan_prediction(request):
    if request.method == 'GET':
        # Retrieve input values from the form
        Gender = int(request.GET.get('n1'))
        Married = int(request.GET.get('n2'))
        Dependents = int(request.GET.get('n3'))
       # Education = (request.GET.get('n4'))
        Self_Employed = int(request.GET.get('n5'))
        ApplicantIncome = float(request.GET.get('n6'))
        #CoapplicantIncome = float(request.GET.get('n7'))
        LoanAmount = float(request.GET.get('n8'))
        Loan_Amount_Term = float(request.GET.get('n9'))
        Credit_History = float(request.GET.get('n10'))
        Property_Area = int(request.GET.get('n11'))
        Collateral=int(request.GET.get('n12'))
        Government_Program = int(request.GET.get('n13'))
        Loan_Purpose = int(request.GET.get('n14'))
        Local_Economic_Factors = int(request.GET.get('n15'))
        Risk_Management_Strategies = int(request.GET.get('n16'))

        # Process categorical variables (you may need to encode them based on how they were encoded during training)
        # For simplicity, I'm using a placeholder encoding here
        gender_encoded = 1 if Gender == 'Male' else 0
        married_encoded = 1 if Married == 'Yes' else 0
        #education_encoded = 1 if Education == 'Graduate' else 0
        self_employed_encoded = 1 if Self_Employed == 'Yes' else 0
        collateral_encoded = 1 if Collateral == 'Yes' else 0
        government_program_encoded = 1 if Government_Program == 'Yes' else 0
        loan_purpose_encoded = 1 if Loan_Purpose == 'Yes' else 0
        local_economic_factors_encoded = 1 if Local_Economic_Factors == 'Yes' else 0
        risk_management_strategies_encoded = 1 if Risk_Management_Strategies == 'Yes' else 0


        # Create a numpy array with the input features
        input_features = np.array([
            [gender_encoded, married_encoded, int(Dependents), self_employed_encoded,
             ApplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
             Property_Area ,collateral_encoded,government_program_encoded,loan_purpose_encoded,local_economic_factors_encoded,risk_management_strategies_encoded]
        ])

        # Load the saved model
        with open('Notebook/modelpkl.pkl', 'rb') as model_file:
            model = pickle.load(model_file)

        # Make predictions
        prediction = model.predict(input_features)
        
        prediction_result = 'Rejected' if prediction[0] == 1 else ' Approved'
        risk_score = model.predict_proba(input_features)[:, 1] * 100  # Assuming the risk score is the probability of being approved (change as needed)
        LoanPrediction.objects.create(result=prediction_result, risk_score=risk_score[0], user=request.user)

        # Display the result
        result = 'Your Loan request is {} , Risk score {:.2f}%'.format(prediction_result, risk_score[0])
        return render(request, 'predict.html', {'result': result})



# ... (remaining code)
@login_required
def view_saved_predictions(request):
    predictions = LoanPrediction.objects.all()
    return render(request, 'saved.html', {'predictions': predictions})

@login_required
def prediction_report(request):
    # Retrieve all saved predictions along with user information
    predictions = LoanPrediction.objects.select_related('user').all()

    context = {'predictions': predictions}
    return render(request, 'prediction_report.html', context)

def custom_logout(request):
    logout(request)
    return redirect('home') 


