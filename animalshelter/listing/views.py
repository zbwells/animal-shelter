from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from django.core.exceptions import FieldError, ValidationError

from .models import *

## Generic view for the index/animal listing
class IndexView(generic.ListView):
    model = Animal
    template_name = "listing/index.html"

    # Sorts and filters out the list of Animals before sending it to the templates.
    # Done via GET parameters (shown in URL, user can bookmark or share page if desired)
    def get_queryset(self):

        # Default parameters for filtering and ordering the animals
        default = Animal.objects.filter(
            ["visible_on_website", True]
        ).order_by("intake_date")

        return default
        

class DetailView(generic.DetailView):
    model = Animal
    template_name = "listing/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if context["animal"].visible_on_website == False:
            del context["animal"]

        return context

# Inherits from the DetailView we've defined
class ExtraView(DetailView):
    template_name = "listing/extra.html"
