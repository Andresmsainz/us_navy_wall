from django.db import models

# Create your models here.
from datetime import datetime

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #1 First & Last Name should be at least 2 characters
        if len(postData['firstname']) < 2:
            errors["firstname"] = "First Name should be at least 2 characters!"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "Last Name should be at least 2 characters!"
        #2 email already exists????  
        if len(User.objects.filter(email=postData["email"])) > 0:
            errors["email"] = "This email already exists. Please Pick Another!"
        #3 check that password and confirm password match
        if postData["password"] != postData["confirmpassword"]:
            errors["password"] = "Passwords do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    #stationed_user = a list of user who are stationed somewhere
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Station(models.Model):
    station_name = models.CharField(max_length=255)
    location = models.CharField(max_length=140,default='Location')
    #stationed_history = a list of stations for the user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class History(models.Model):
    division = models.CharField(max_length=50)
    #from_year = models.CharField(max_length=4)
    from_year = models.IntegerField(default=0)
    #to_year = models.CharField(max_length=4)
    to_year = models.IntegerField(default=0)
    user_stationed = models.ForeignKey(User, related_name="stationed_user", on_delete = models.CASCADE)
    #the user who was stationed in this station
    history_stationed = models.ForeignKey(Station, related_name="stationed_history", on_delete = models.CASCADE)
    #a list of stattions for this user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
