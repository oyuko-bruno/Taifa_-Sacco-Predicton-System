from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class CustomerPrediction(models.Model):
    gender = models.IntegerField()
    married = models.IntegerField()
    dependents = models.IntegerField()
    education = models.IntegerField()
    self_employed = models.IntegerField()
    applicant_income = models.FloatField()
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()
    credit_history = models.FloatField()
    property_area = models.IntegerField()
    result = models.IntegerField()

    def __str__(self):
        return f"Prediction for {self.id}"


from django.db import models
from django.conf import settings


# models.py
from django.db import models
from authentication.models import CustomUser  # Adjust the import based on your actual project structure
from authentication.models import CustomUser

class LoanPrediction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
    risk_score = models.FloatField() 
