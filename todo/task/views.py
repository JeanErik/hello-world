from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("here are my tasks")