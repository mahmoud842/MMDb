from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

def index(request):
    date = datetime.now()
    return render(request, "filmsList/index.html",{
        'year':date.year,
        'month':date.month,
        'day':date.day
    })
