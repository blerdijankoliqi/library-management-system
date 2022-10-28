from django.contrib import admin
from django.urls import path, include
from .views import renderLoginPage, renderDashboardPage, renderBasePage

urlpatterns = [
    path('', renderLoginPage, name='home' ),
    path('base/', renderBasePage, name='base'),
    path('dashboard/', renderDashboardPage, name='dashboard'),
]
