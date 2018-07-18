from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def index(request):
    date = dt.date.today()

    return render(request, 'index.html')

def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day