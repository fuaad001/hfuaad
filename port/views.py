from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import *

def index(request):

    works = Project.objects.all()

    return render(request, 'index.html', {"works":works})

def projects(request):

    works = Project.objects.all()
    angular = Project.objects.filter(technologies__icontains='Angular').all()
    collaborations = Project.objects.filter(description__icontains='collaboration').all()
    django = Project.objects.filter(technologies__icontains='Django').all()
    flask = Project.objects.filter(technologies__icontains='Flask').all()
    javascript = Project.objects.filter(technologies__icontains='Javascript').all()

    return render(request, 'projects.html', {"works":works, "angular":angular,"collaborations":collaborations,"django":django,"flask":flask,"javascript":javascript,})

def contact(request):

    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')
