from django.shortcuts import render
from .models import Project
import requests


def home(request):
    return render(request, "Pages/home.html")


def projects(request):
    projects_list = Project.objects.all().order_by("-id")

    context = {
        "projects": projects_list,
    }

    return render(request, "Pages/projects.html", context)


def skills(request):
    return render(request, "Pages/skills.html")


def contact(request):
    return render(request, "Pages/contact.html")


def dashboard(request):
    return render(request, "Pages/dashboard.html")