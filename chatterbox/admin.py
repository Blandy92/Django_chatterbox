from django.contrib import admin

# Register your models here.
from chatterbox.models import Room, Message

admin.site.register(Room)
admin.site.register(Message)
