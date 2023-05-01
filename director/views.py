from django.shortcuts import render
from .models import Director

# Create your views here.
def render_directors(request):
    directors = Director.objects.all()

    return render(request, 'directors.html',{'directors':directors})