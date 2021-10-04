from django.http import request,HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from .models import Appeal, About, Picture, Vacancy
# Create your views here.

def index(request):
    about = About.objects.all()
    gallery_list = Picture.objects.all()
    return render(request, "admining/index.html", {'about': about, 'gallery': gallery_list})

def vacancy(request):
    vacancy_list = Vacancy.objects.all()
    return render(request, "admining/elements.html", {"vacancy":vacancy_list})

def leave_appeal(request):
    a= Appeal.objects.all()
    a.create(appealer_name = request.POST['name'],appealer_email = request.POST['email'], appealer_message = request.POST['message'])
    return HttpResponseRedirect( reverse('admining:index'))
