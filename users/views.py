from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        context = {
            'form' :  LoginForm()
        }

        return render(request, 'users/login.html', context)

    elif request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi  {username.title()}, Wellcome back')
                return redirect('home')

        #invalid username and password
        messages.error(request, f'Invalid user or password!')
        return render(request, 'users/login.html', {'form' : form })

def sign_out(request):
    logout(request)
    messages.success(request, 'You have been logout')
    return redirect('login')


