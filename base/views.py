from django.shortcuts import render


# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Django is awesome'},
    {'id': 3, 'name': 'full stack development'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')
