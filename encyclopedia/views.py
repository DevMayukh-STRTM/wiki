from django.shortcuts import render
from django import forms
from encyclopedia.util import *
import random
 
from . import util

class NewForm(forms.Form):
    q = forms.CharField(label="Search Entry")

def index(request):
    lis = list_entries()
    reber = random.choice(lis)
    namex = None
    if request.method == 'GET':
        ax = NewForm(request.GET)
        if ax.is_valid():
            axx = ax.cleaned_data["q"]
            htmldata = util.search(axx)
            if len(htmldata) == 1:
                namex = "Result"
            elif len(htmldata) == 0:
                namex = "Result"
            else:
                namex = "Results"

            return render(request, "encyclopedia/index.html", {
                "entries": htmldata,
                "Name": f"Search Result for '{axx}', {len(htmldata)} {namex} Found",
                "form": NewForm()
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "Name": "All Entries",
        "form": NewForm(),
        "rand": f"wiki/{reber}"
    })

