# admin.py 
#admin.py
from django.contrib import admin
from .models import CustomerPrediction
from .models import LoanPrediction

admin.site.register(CustomerPrediction)
admin.site.register(LoanPrediction)



