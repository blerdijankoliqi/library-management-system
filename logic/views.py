from django.shortcuts import render
from .models import Student

# Create your views here.
def renderNames(request):
    return render(request, 'login.html')

