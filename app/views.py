from datetime import datetime

from django.shortcuts import render


def home(request):
    date = datetime.now().date()
    name = 'Dave'
    return render(request, 'home.html',{
        'date': date, 'name': name
    })


