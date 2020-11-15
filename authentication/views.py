from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def register(request):
    return

def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return