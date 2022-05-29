from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")

class Director(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")

class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")

class Clerk(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")

class Category(models.Model):
    type = models.CharField(max_length=50, blank=False, null=False, default="")

class Classification(models.Model):
    age = models.IntegerField(null=False, blank=False, default=None)  

class Film(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default="")
    duration = models.CharField(max_length=30, blank=False, null=False, default="")
    fk_atores = models.ManyToManyField(Actor)
    fk_classification = models.ForeignKey(Classification ,blank=False, null=False, default="", on_delete=models.CASCADE)
    fk_category = models.ForeignKey(Category ,blank=False, null=False, default="", on_delete=models.CASCADE)

class Room(models.Model):
    room_number = models.IntegerField(null=False, blank=False, default=None)

class Session(models.Model):
    fk_film = models.ForeignKey(Film, blank=False, null=False, default="", on_delete=models.CASCADE)
    fk_room = models.ForeignKey(Room, blank=False, null=False, default="", on_delete=models.CASCADE)

class Ticket(models.Model):
    film_date = models.DateTimeField(auto_now_add=False, blank=False, null=False, default=None)
    fk_session= models.ForeignKey(Session, blank=False, null=False, default="", on_delete=models.CASCADE)
    fk_client = models.ForeignKey(Client, blank=False, null=False, default="", on_delete=models.CASCADE)
    fk_clerk = models.ForeignKey(Clerk, blank=False, null=False, default="", on_delete=models.CASCADE)


