from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name':'Lets learn Python'},
    {'id': 2, 'name':'Django is awesome'},
    {'id': 3, 'name':'full stack development'},
]

def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
