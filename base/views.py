from django.shortcuts import render


rooms = [
    # {'id', 'name':'Calculus made easy'},
    {'id':1, 'name':'Engineers on board'},
    {'id':2, 'name':'Technical geeks'},
    {'id':3,  'name':'Lets program'},
]


def home(request):
    return  render(request, 'home.html')

def room(request):
    return render(request, 'room.html')   





