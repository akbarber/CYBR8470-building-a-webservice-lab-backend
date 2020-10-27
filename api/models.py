from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Dog(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField()
    breed = models.ForeignKey( #not done
        Breed, 
        on_delete=models.CASCADE
    )
    gender = models.CharField(max_length=1000, blank=False)
    color = models.CharField(max_length=1000, blank=False)
    favoritefood = models.CharField(max_length=1000, blank=False)
    favoritetoy = models.CharField(max_length=1000, blank=False)
    


class Breed(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    size = models.CharField(max_length=1000, blank=False) #need to make sure only accepts the 4 options
    friendliness = models.IntegerField(min_value=1, max_length=5, blank=False) #put in validator
    trainability = models.IntegerField(min_value=1, max_length=5, blank=False)
    sheddingamount = models.IntegerField(min_value=1, max_length=5, blank=False)
    exerciseneeds = models.IntegerField(min_value=1, max_length=5, blank=False)


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
