from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from datetime import datetime
import csv

class AddNewForm(forms.Form):
    name = forms.CharField(label="Name")
    language = forms.CharField(label="language")
    year = forms.IntegerField(label="Year" , max_value=3000)
    rate = forms.FloatField(label="rating")



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
    
def addFilm(request):

    if request.method == "POST":
        form = AddNewForm(request.POST)

        if form.is_valid():
            fieldNames = [
                'name',
                'language',
                'year',
                'rating'
            ]
            with open('films.csv', 'a' ,newline='\n') as filmscsv:
                write = csv.DictWriter(filmscsv, fieldnames=fieldNames)
                write.writerow({
                    'name': form.cleaned_data['name'],
                    'language': form.cleaned_data['language'],
                    'year': form.cleaned_data['year'],
                    'rating': form.cleaned_data['rate']
                })

    return render(request, "filmsList/addFilm.html",{
        'form': AddNewForm()
    })
