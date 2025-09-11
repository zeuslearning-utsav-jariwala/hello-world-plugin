"""
URLs for hello_world.
"""
from django.urls import path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import hello_world_view

urlpatterns = [
    path('', hello_world_view, name='hello_world'),
]
