from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from chatterbox.models import Room, Message


def hello(request, s):
    return HttpResponse(f'Hello, {s} world!!!')


def home(request):
    rooms = Room.objects.all()  # najdeme vsetky miestnosti

    context = {'rooms': rooms}
    return render(request, 'chatterbox/home.html', context)


def search(request, s):
    rooms = Room.objects.filter(name__contains=s)
    # response = "Rooms: "
    # for room in rooms:
    #     response += room.name + ", "

    messages = Message.objects.filter(body__contains=s)
    # response += "<br>Message: "
    # for message in messages:
    #     response += message.body[0:10] + "... ,"

    context = {'rooms': rooms, 'messages': messages}
    return render(request, "chatterbox/search.html", context)


def room(request, pk):
    room = Room.objects.get(id=pk)  # najdeme konkretnu miestnost so zadanym id
    messages = Message.objects.filter(room=pk)  #vyberieme vsetky spravy v danej miestnosti

    context = {'room': room, 'messages': messages}
    return render(request, "chatterbox/room.html", context)
