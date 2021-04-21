from django.db import models
from django.contrib.postgres.fields import ArrayField

class Song(models.Model()):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100,null=False,blank=False)
    Song_Duration = models.PositiveIntegerField()
    Upload_Time = models.DateTimeField(auto_now_add=True,blank=False)
    created_by = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)

class Podcast(models.Model()):
    ID = models.IntegerField(primary_key=True)
    Podcast_Name = models.CharField(max_length=100,null=False,blank=False)
    Podcast_Duration = models.PositiveIntegerField()
    Upload_Time = models.DateTimeField(auto_now_add=True,blank=False)
    Host = models.CharField(max_length=100,null=False,blank=False)
    Participants = ArrayField(models.CharField(max_length=100),size=10,blank=True,null=True)
    created_by = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)

class Audiobook(models.Model()):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=100,blank=False,null=False)
    Author = models.CharField(max_length=100,blank=False,null=False)
    Narrator = models.CharField(max_length=100,blank=False,null=False)
    Audiobook_Duration = models.PositiveIntegerField()
    Upload_Time = models.DateTimeField(auto_now_add=True,blank=False)
    created_by = models.CharField()
    created_on = models.DateTimeField(auto_now_add=True)