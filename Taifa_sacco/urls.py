"""
URL configuration for Taifa_sacco project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views
from django.urls import include, path
from .views import loan_prediction, view_saved_predictions,prediction_report
from .views import custom_logout
from .views import chat

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', views.home ,name='home'),
    #path('loan_prediction/', loan_prediction, name='loan_prediction'),
    path('predict/', views.predict, name='predict'),
    path('predict/loan_prediction/', views.loan_prediction, name='loan_prediction'),
    path('authentication/', include('authentication.urls'), name='authentication'),
    path('saved/', view_saved_predictions, name='view_saved_predictions'),
    path('report/', prediction_report, name='prediction_report'),
    path('logout/', custom_logout, name='logout'),
    
    path('', chat, name='chat'),

   
 # Add a name for the result view
]

admin.site.site_header = "Taifa Sacco Admin"
admin.site.site_title = "Taifa Sacco Admin Portal"
admin.site.index_title = "Welcome to Taifa Sacco  Portal"
# your_project/urls.py


from django.urls import path








