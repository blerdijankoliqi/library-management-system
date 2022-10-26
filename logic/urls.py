from django.contrib import admin
from django.urls import path, include
from .views import renderLoginPage, renderDashboardPage

urlpatterns = [
    path('', renderLoginPage, name='home' ),
    path('base/', renderDashboardPage, name='base'),
]
