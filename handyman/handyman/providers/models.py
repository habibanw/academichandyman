import datetime

from django.db import models


# Create your models here.
# class Handyman:
#     def __init__(self, id, name, email, services, description, date_created):
#         self.id = id
#         self.name = name
#         self.email = email
#         self.services = services
#         self.description = description
#         self.date_created = date_created
#
#
#
# providers = []


class Handyman(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    services = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    average_rating = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name


regularUser = {"username": 'username', "password": 'password'}
