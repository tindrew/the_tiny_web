from django.shortcuts import render, redirect
from . forms import CreateUserForm

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

def home(request):
    
    return render(request, 'account/index.html')


def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('user_login')
    
    context = {'RegisterForm': form}
    
    return render(request, 'account/register.html', context)






def user_login(request):
    
   
    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username') # Username / Email
            password = request.POST.get('password')

            # Username / Email

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect('user-dashboard')


            # if user is not None and user.is_writer==False:

            #     login(request, user)

            #     return HttpResponse('client-dashboard')


    context = {'LoginForm': form}

    return render(request, 'account/user_login.html', context)

def user_logout(request):
    
    logout(request)
    
    return redirect('user-login')



