# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Trip(models.Model):
    destination=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    users=models.ManyToManyField(User, related_name="users")
    created_by=models.ForeignKey(User, related_name="cUsers")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
