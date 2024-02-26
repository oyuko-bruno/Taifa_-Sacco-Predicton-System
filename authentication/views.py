from django.shortcuts import render

# Create your views here.
# authentication/views.py

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')

            # Redirect to user_login page with customer_name in the URL
            return redirect('user_login')

    else:
        form = RegistrationForm()
        
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('predict')  # Redirect to home page or any other page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
    #return render_template('register.html', msg = msg)
@login_required
def update_account(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('predict')  # Redirect to the same update_account page
    else:
        form = RegistrationForm(instance=request.user)
    return render(request, 'update_account.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Account deleted successfully.')
        return redirect('registe')  # Redirect to the login page or any other page

    return render(request, 'delete_account.html')


