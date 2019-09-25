from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    return render(request, "index.html", {"menus": menus, "profile": profile})

