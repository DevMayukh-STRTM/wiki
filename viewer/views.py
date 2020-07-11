from django import forms
from django.shortcuts import render
from encyclopedia.util import *

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class NewEditForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'container-fluid', 'value': "{{ title }}"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'container-fluid', 'rows': '10', 'value': '{{ content }}'}))

def index(request, entryname):
    list_of_entries = list_entries()
    if entryname in list_of_entries:
        header = "{% extends 'editor/editor.html' %}"
        title = "{% block cardname %}"
        end = "{% endblock %}"
        body = "{% block card-body %}"
        button = "{% block button %}"


        html = HtmlMk(entryname)
        final_entry = f'{header}{title}{entryname}{end}{body}{html}{end}{button}<a href="edit/{entryname}">Edit File</a>{end}'

        file_path = "viewer/templates/files/index.html"

        if default_storage.exists(file_path):
            default_storage.delete(file_path)
    
        default_storage.save(file_path, ContentFile(final_entry))
        return render(request, 'files/index.html', {
            'status': "display: none;"
        })

    else:
        header = "{% extends 'editor/editor.html' %}"
        title = "{% block cardname %}"
        end = "{% endblock %}"
        body = "{% block card-body %}"
        button = "{% block button %}"

                                                                         
        final_entry = f'{header}{title}Error 404{end}{body}Entry not Valid or is inexistent{end}{button}{end}'

        file_path = "viewer/templates/files/index.html"

        if default_storage.exists(file_path):
            default_storage.delete(file_path)
    
        default_storage.save(file_path, ContentFile(final_entry))
        return render(request, 'files/index.html', {
            "select": "display: none;",
            'status': "display: none;"
        })

def edit(request, name):
    if request.method == "POST":
        ax = NewEditForm(request.POST)
        if ax.is_valid():
            title = ax.cleaned_data["title"]
            content = ax.cleaned_data["content"]
            save_entry(title, content)
            return render(request, 'files/form.html', {
                "file": name, "select": "display: none;", "title": name, "content": get_entry(name), "form": NewEditForm(), "message": "Updated Entry Successfully", "contes": "alert alert-success"})
    return render(request, 'files/form.html', {
        "file": name,
        "select": "display: none;",
        "title": name,
        "content": get_entry(name),
        "form": NewEditForm()
    })

