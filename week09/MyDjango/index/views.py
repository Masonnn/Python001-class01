from django.shortcuts import render, redirect
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("Hello Homepage!")


def login_fail(request):
    return render(request, 'login_fail.html')


def login_success(request):
    return render(request, 'login_success.html')


def log_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/login_success')
            else:
                return redirect('/login_fail')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})
