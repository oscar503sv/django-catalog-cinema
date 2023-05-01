from django.urls import path
from .views import render_directors

urlpatterns = [
    path('', render_directors, name='directors')
]
