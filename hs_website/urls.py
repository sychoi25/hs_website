from django.urls import path

from website import views
from website import admin

urlpatterns = [
    path('', views.home, name='home')
]