## Amber Shackleford.
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.

from django.http import HttpResponse

class News(generic.ListView):
	model = Post
	template_name = "news/news.html"
	def get_queryset(self):
		default = Post.objects.all().order_by("-pub_date")
		return default
		
def post_list(request):
	queryset = Post.objects.all()
	
	return render(request)
