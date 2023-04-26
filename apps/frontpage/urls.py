## Amber Shackleford.
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django.urls import path 
from . import views

urlpatterns = [
	path("", views.home, name = "home"),
	path("contact", views.contact, name = "contact"),
	path("about", views.about, name = "about"),
]
