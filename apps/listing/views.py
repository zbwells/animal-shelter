## Zander B. Wells <zbwells@protonmail.com>
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.


from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.exceptions import FieldError, ValidationError

from .models import *
from .forms import *

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
        
        try:
            filter_by_age = self.request.GET.get(
                "filter_by_age",
                "any-age"
            )

            filter_by_species = self.request.GET.get(
                "filter_by_species",
                "any-species"
            )
            
            order = self.request.GET.get("order", "intake_date")
            
            # Handle age order case
            if order == "estimated_age":
                order = ["estimated_age", "estimated_age_months"]
            
            queries = []
            queries.append(["visible_on_website", True])

            # Handle the age filter's special cases (so, all cases)
            # These correlate to the options specified in forms.py
            if filter_by_age == "any-age":
                pass
                
            elif filter_by_age == "two-or-more-years":
                queries.append(["estimated_age__gt", "1"])

            elif filter_by_age == "three-or-more-years":
                queries.append(["estimated_age__gt", "2"])
                    
            elif filter_by_age == "zero-to-two-months":
                queries.append([
                    "estimated_age_months__in", 
                    ['0', '1', '2']
                ])
                
                queries.append(["estimated_age__lt", '1'])

            elif filter_by_age == "three-to-six-months":
                queries.append([
                    "estimated_age_months__in",
                    ['3', '4', '5', '6']
                ])

                queries.append(["estimated_age__lt", '1'])
                
            elif filter_by_age == "seven-to-eleven-months":
                queries.append([
                    "estimated_age_months__in",
                    ['7', '8', '9', '10', '11']
                ])

                queries.append(["estimated_age__lt", '1'])

            elif filter_by_age == "one-to-two-years":
                queries.append(["estimated_age__in", ['1', '2']])

            # Deal with cases for species filtering
            # Same as before, look at forms.py for options to handle
            if filter_by_species == "any-species":
                pass
            else:
                queries.append(["species__in", 
                    [
                        filter_by_species, 
                        filter_by_species.capitalize(),
                        filter_by_species.upper(),
                    ]
                ])
                
            queryset = Animal.objects

            # Apply all filters
            for lst in queries:
                queryset = queryset.filter(lst)

            # Apply ordering/sorting
            # If ordering by more than one thing, use starred expression
            if isinstance(order, list):
                queryset = queryset.order_by(*order)
            elif isinstance(order, str):
                queryset = queryset.order_by(order)
            

        # If the GET request is malformed, fall back on a default listing setup        
        except (FieldError, ValidationError, ValueError):
            return default

        return queryset

    # Adds our filter form from forms.py
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = FilterForm(self.request.GET or None)
            
        context["order"] = str(self.request.GET.get("order")).replace("_", " ")
        
        age_filter = str(self.request.GET.get("filter_by_age"))
        context["age_filter"] = age_filter.replace("-", " ")

        species_filter = str(self.request.GET.get("filter_by_species"))
        context["species_filter"] = species_filter
        
        return context
        

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
