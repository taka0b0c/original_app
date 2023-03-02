from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    return render(request, "admin.html")

def detail(request):
    return render(request, "detail.html")

def results(request):
    return render(request, "results.html")

def vote(request):
    return render(request, "vote.html")