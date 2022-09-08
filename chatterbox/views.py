from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from chatterbox.models import Room, Message


def hello(request, s):
    return HttpResponse(f'Hello, {s} world!!!')


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
