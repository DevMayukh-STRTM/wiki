from django.shortcuts import render
from encyclopedia.util import *
from django import forms

# Create your views here.
class NewEditForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'container-fluid', 'value': "{{ title }}"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'container-fluid', 'rows': '10', 'value': '{{ content }}'}))

def index(request):
    if request.method == "POST":
        ax = NewEditForm(request.POST)
        if ax.is_valid():
            title = ax.cleaned_data["title"]
            content = ax.cleaned_data["content"]
            save_entry(title, content)
            return render(request, 'files/forms.html', { "select": "display: none;", "form": NewEditForm(), "message": "Added New Entry Successfully", "contes": "alert alert-success"})
    return render(request, 'files/forms.html', {
        "select": "display: none;",
        "form": NewEditForm()
    })
