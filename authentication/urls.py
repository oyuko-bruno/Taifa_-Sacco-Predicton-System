
app_name = 'authentication'
from django.urls import path
from .views import register, user_login, update_account, delete_account

urlpatterns = [
    path('register/', register, name='register'),
    path('user_login/', user_login, name='login'),
    path('update_account/', update_account, name='update_account'),
    path('delete_account/', delete_account, name='delete_account'),
    
    
]
