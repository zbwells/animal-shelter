from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
	return render(request, "frontpage/home.html",{})

def contact(request):
	return render(request, "frontpage/contact.html",{})

def about(request):
	return render(request, "frontpage/about.html",{})
	

