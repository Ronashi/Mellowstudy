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
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            context = {'room':room}
    return render(request, 'base/room.html',context)   






