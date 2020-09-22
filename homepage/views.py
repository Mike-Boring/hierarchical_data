from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Hierarchy

from homepage.forms import AddFileForm

# Create your views here.


def index(request):
    tree = Hierarchy.objects.all()
    return render(request, "index.html", {"tree": tree})


def addfile(request):
    file_names = Hierarchy.objects.all()
    if request.method == "POST":
        form = AddFileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if Hierarchy.objects.filter(name=data.get('name')):
                form = AddFileForm()
                message = '- Please pick a unique file name -'
                return render(request, "generic_form.html", {"form": form, "message": message})
            else:
                new_file = Hierarchy.objects.create(
                    name=data.get('name'),
                    parent=data.get('parent'),
                )
                return HttpResponseRedirect(reverse("homepage"))

    form = AddFileForm()
    return render(request, "generic_form.html", {"form": form})
