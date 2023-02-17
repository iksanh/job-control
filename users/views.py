from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
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


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return  render(request, 'users/registration.html', {'form' : form})

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singeng up successfully')
            login(request, user)
            return redirect('home')

        else:
            return render(request, 'users/registration.html', {'form' :  form})


