## Zander B. Wells <zbwells@protonmail.com>
## Part of the Wise Animal Shelter Management System Project.
##
## Released under the terms of the MIT License.
## See LICENSE for details.

# File to contain all of the urls for the animal listings.

from django.urls import path
from . import views

urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        path("extra/<int:pk>/", views.ExtraView.as_view(), name="extra"),
]
