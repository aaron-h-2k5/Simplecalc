from django.urls import re_path as url
from . import views

urlpatterns = [
    # redirect to simpleCalc view as a function
    url(r'^$',
        views.simpleCalc,
        name='simpleCalc'
        ),
]
