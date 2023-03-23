# File to contain all of the urls for the animal listings.

from django.urls import path
from . import views

urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>/", views.DetailView.as_view(), name="detail"),
        path("extra/<int:pk>/", views.ExtraView.as_view(), name="extra"),
]
