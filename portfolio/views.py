from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    menus = Menu.get_all_menus()
    return render(request, "index.html", {"menus": menus})

