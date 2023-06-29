from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
import csv

def index(request):

    with open('films.csv', newline='') as filmscsv:
        films_dict = csv.DictReader(filmscsv)
        date = datetime.now()
        return render(request, "filmsList/index.html",{
            'year':date.year,
            'month':date.month,
            'day':date.day,
            'films':films_dict
        })
