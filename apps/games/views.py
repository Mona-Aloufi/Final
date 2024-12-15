from django.shortcuts import render
from .models import Game
from django.template import loader

def home(request):
    return render(request,"games/home.html")
def list(request):
    games=Game.objects.all()
    return render(request,"games/list.html",{"games":games})
