from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    # filter_horizontal = ('profiles',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Clerk)
class ClerkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', )

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'age', )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','duration' )
    filter_horizontal = ('fk_atores',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_number',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_film','fk_room')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'film_date','fk_session','fk_client','fk_clerk')