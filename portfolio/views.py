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
    projects = Project.get_all_projects()
    return render(
        request,
        "projects.html",
        {"menus": menus, "profile": profile, "projects": projects},
    )


def project(request, id):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    project = Project.get_single_project(id)
    images = ProjectImage.get_images_of_project(id)
    technologies = ProjectTech.get_technologies_of_project(id)
    return render(
        request,
        "project.html",
        {
            "menus": menus,
            "profile": profile,
            "project": project,
            "images": images,
            "technologies": technologies,
        },
    )


def contacts(request):
    menus = Menu.get_all_menus()
    profile = Profile.get_profile()
    return render(request, "contacts.html", {"menus": menus, "profile": profile})
