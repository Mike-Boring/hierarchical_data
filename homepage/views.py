from django.shortcuts import render

from homepage.models import Hierarchy

# Create your views here.


def index(request):
    tree = Hierarchy.objects.all()
    return render(request, "index.html", {"tree": tree})
