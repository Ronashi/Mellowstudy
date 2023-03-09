from django.shortcuts import render


rooms = [
    
    {'id':1, 'name':'Engineers on board'},
    {'id':2, 'name':'Technical geeks'},
    {'id':3,  'name':'Lets program'},
]


# def home(request):
#     return  render(request, 'home.html', {'rooms': rooms})


def home(request):
    context = {'rooms':rooms}
    return  render(request, 'base/home.html', context)

def room(request,pk):
    return render(request, 'room.html')   






