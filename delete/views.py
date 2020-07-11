from django.shortcuts import render
from encyclopedia.util import *
# Create your views here.

def index(request, query):
    check = deleteFile(query)
    if check:
        return render(request, 'files/deleted.html', {
            "status": "Success"
        })
    else:
        return render(request, 'files/deleted.html', {
            "status": "exeption"
        })
