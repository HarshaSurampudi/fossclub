from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
# Create your views here.
from django.template import loader


def index(request):
    is_logged_in = False
    if request.user.is_authenticated:
        is_logged_in = True
        username = request.user.username
        project_list = Project.objects.all()
        context = {"project_list": project_list, "username": username, "is_logged_in": is_logged_in}
        template = loader.get_template('home.html')
        return HttpResponse(template.render(context, request))
    template = loader.get_template('home.html')
    context = {"is_logged_in": is_logged_in}
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    template = loader.get_template('signup.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))


def logout_request(request):
    logout(request)
    return redirect('index')


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"form": form}
    template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))


def project(request, project_id):
    if request.user.is_authenticated:
        is_logged_in = True;
        proj = Project.objects.get(pk=project_id)
        if proj is None:
            return redirect('/')
        context = {"proj":proj, "is_logged_in": is_logged_in}
        template = loader.get_template('project.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/')
