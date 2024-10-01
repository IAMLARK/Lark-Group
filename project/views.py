from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .forms import SignUpForm



# @unauthenticated_user
def login_user(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged in!")

            if user.groups.filter(name='admin').exists():
                return redirect('admin_dashboard')  
            elif user.groups.filter(name='customer').exists():
                return redirect('customer_dashboard') 
            elif user.groups.filter(name='technician').exists():
                return redirect('tech_dashboard') 
            else:
                return redirect('default_dashboard') 

        else:
            messages.error(request, "There was an Error logging in Please try again...")
            return redirect('login')
     else:
        return render(request, 'login.html', )
     
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticte and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user )
            messages.success(request, "You have succesfully registered Welcome")
            return redirect('login')
    else: 
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})
        

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged out...")
    return redirect('login')   

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin',])
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['finance',])
def finance_dashboard(request):
    return render(request, 'finance/finance_dashboard.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['technician',])
def tech_dashboard(request):
    return render(request, 'technician/tech_dashboard.html')


def home(request):
    return render(request, 'home.html')


