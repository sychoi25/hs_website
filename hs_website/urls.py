from django.urls import path

from website import views
from website import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
]