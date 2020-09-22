from django import forms
from homepage.models import Hierarchy


class AddFileForm(forms.Form):
    file_names = Hierarchy.objects.all()
    name = forms.CharField(max_length=200)
    parent = forms.ModelChoiceField(file_names)
