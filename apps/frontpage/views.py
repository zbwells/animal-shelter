## Amber Shackleford.
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
	return render(request, "frontpage/home.html",{})

def contact(request):
	return render(request, "frontpage/contact.html",{})

def about(request):
	return render(request, "frontpage/about.html",{})
	

