from django.shortcuts import render
from .models import User

# Create your views here.

def signup(request):
    return render(request, 'SignUp/signup.html')

