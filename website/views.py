
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = locals()
    layout = 'home.html'
    return render(request, layout, context)