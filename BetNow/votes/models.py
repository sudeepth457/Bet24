from django.db import models

# Create your models here.
class uservotes(models.Model):
    mnumber = models.CharField(max_length=20)
    uname = models.CharField(max_length=500,default=0)
    teamone = models.IntegerField(default=0)
    teamtwo = models.IntegerField(default=0)
    is_voted = models.CharField(default=0,max_length=20)
    vote =  models.IntegerField(default=0)
    team = models.CharField(max_length=50)
    money = models.IntegerField(default=0)



    def __str__(self):
        return self.uname





    

