from django.shortcuts import render
from .models import Student

# Create your views here.
def renderLoginPage(request):
    return render(request, 'login.html')

def renderDashboardPage(request):
    return render(request, 'base.html')

