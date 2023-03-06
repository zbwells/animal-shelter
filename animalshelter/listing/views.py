from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Animal, Picture

## Generic view for the index/animal listing
class IndexView(generic.ListView):
    template_name = "listing/index.html"
    context_object_name = "animal_list"

    get_queryset = lambda self: Animal.objects.order_by("-intake_date")

class DetailView(generic.DetailView):
    model = Animal
    template_name = "listing/detail.html"
