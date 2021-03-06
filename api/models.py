from __future__ import unicode_literals

from django.db import models
from django.core.validators import *
#from model_utils import Choices

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64


class Dog(models.Model):
    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=True) #, related_name='breeds'
    gender = models.CharField(max_length=10, blank=False)
    color = models.CharField(max_length=25, blank=False)
    favoritefood = models.CharField(max_length=50, blank=False)
    favoritetoy = models.CharField(max_length=25, blank=False)
 
        
    def __str__(self):
        return str(self.name) + str(self.gender) + str(self.color) + str(self.favoritefood) + str(self.favoritetoy)

class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'color', 'favoritefood', 'favoritetoy', 'breed')           

class Breed(models.Model):
    SIZE = (
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    )
# subclasses below if i want to try IntegerChoices    

    name = models.CharField(max_length=50, blank=False)
    size = models.CharField(max_length=6, blank=False, choices=SIZE) 
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    sheddingamount = models.IntegerField()
    exerciseneeds = models.IntegerField()

    def __str__(self):
        return str(self.name) + str(self.size)

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds')

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')
 



#  class Friendliness(models.IntegerChoices):
#         VERY_UNFRIENDLY = 1
#         UNFRIENDLY = 2
#         AVERAGE = 3
#         VERY_FRIENDLY = 4
#         VERY_FRIENDLY = 5

#     class Trainability(models.IntegerChoices):
#         NOT_TRAINABLE = 1
#         UNFRIENDLY = 2
#         AVERAGE = 3
#         VERY_FRIENDLY = 4
#         VERY_FRIENDLY = 5

#     class Sheddingamount(models.IntegerChoices):
#         VERY_UNFRIENDLY = 1
#         UNFRIENDLY = 2
#         AVERAGE = 3
#         VERY_FRIENDLY = 4
#         VERY_FRIENDLY = 5

#     class Exerciseneeds(models.IntegerChoices):
#         VERY_UNFRIENDLY = 1
#         UNFRIENDLY = 2
#         AVERAGE = 3
#         VERY_FRIENDLY = 4
#         VERY_FRIENDLY = 5