from datetime import timezone
import datetime
from enum import Enum
from django.db import models

class GameStatus(Enum):
    INITIATED = "INITIATED"
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ERROR = "ERROR"
    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    
class Player(models.Model):
    question_text = models.CharField(max_length=200)
    username = models.CharField(max_length=80)

class Action(models.Model):
    text = models.CharField(max_length=500)
    def __str__(self):
        return self.text
    
class Game(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=80)
    type = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    state = models.CharField(max_length=255, choices=GameStatus.choices())
    winner = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        

    
