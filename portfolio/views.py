from django.shortcuts import render
import random
from .models import *

# Create your views here.
def home(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    mistari = Quote.get_all_quotes()
    mstari = random.choice(mistari)
    return render(
        request, "home.html", {"menus": menus, "profile": profile, "mstari": mstari}
    )


def about(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    categories = SkillCategory.get_all_categories()
    technologies = Technology.get_technologies_in_category()
    # print(technologies)
    return render(
        request,
        "about.html",
        {
            "menus": menus,
            "profile": profile,
            "categories": categories,
            "technologies": technologies,
        },
    )


def projects(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    return render(request, "about.html", {"menus": menus, "profile": profile})


def contacts(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    return render(request, "about.html", {"menus": menus, "profile": profile})
