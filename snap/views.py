from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .models import Image
import pyperclip

# Create your views here.
def index(request):
    date = dt.date.today()
    image = Image.get_all()

    return render(request, 'index.html', {"image":image})

def get_location(request, location):
    image = Image.filter_location(location)
    return render(request, 'location.html', locals())

def get_category(request, category):
    image = Image.filter_category(category)
    return render(request, 'category.html', locals())
    


def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day