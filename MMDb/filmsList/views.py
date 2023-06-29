from django.shortcuts import render
from django.http import HttpResponse
from django import forms

from datetime import datetime
import csv

class AddNewForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'input_area', 'placeholder': 'name'}))
    language = forms.CharField(label="language", widget=forms.TextInput(attrs={'class': 'input_area', 'placeholder':'language'}))
    year = forms.IntegerField(label="Year",
                              widget=forms.TextInput(attrs={'class': 'input_area' , 'placeholder':'year'}),
                              max_value=3000
                            )
    rate = forms.FloatField(label="Rating" , widget=forms.TextInput(attrs={'class': 'input_area' , 'placeholder':'rate'}))
    type = forms.CharField(label="Type" , widget=forms.TextInput(attrs={'class': 'input_area' , 'placeholder':'type'}))



def index(request):

    with open('films.csv', newline='') as filmscsv:
        films_dict = csv.DictReader(filmscsv)
        date = datetime.now()
        return render(request, "filmsList/index.html",{
            'year':date.year,
            'month':date.month,
            'day':date.day,
            'films':films_dict,
        })
    
def addFilm(request):

    if request.method == "POST":
        form = AddNewForm(request.POST)

        if form.is_valid():
            fieldNames = [
                'name',
                'language',
                'year',
                'rating',
                'type'
            ]
            with open('films.csv', 'a' ,newline='\n') as filmscsv:
                write = csv.DictWriter(filmscsv, fieldnames=fieldNames)
                write.writerow({
                    'name': form.cleaned_data['name'],
                    'language': form.cleaned_data['language'],
                    'year': form.cleaned_data['year'],
                    'rating': form.cleaned_data['rate'],
                    'type': form.cleaned_data['type']
                })

    return render(request, "filmsList/addFilm.html",{
        'form': AddNewForm()
    })
