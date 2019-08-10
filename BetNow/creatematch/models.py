from django.shortcuts import reverse
# Create your models here.
from django.db import models
# Create your models here.
from .operations import GenerateOTP
class match(models.Model):
    category_choice = (
        ('cricket', 'Cricket'),
        ('kabbadi', 'Kabbadi'),
        ('football', 'FootBall')
    )
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    stadium = models.CharField(max_length=1000)
    city  = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=False)
    matchno = models.IntegerField()
    matchId = models.CharField(primary_key=True, max_length=5, default=GenerateOTP)
    category = models.CharField(max_length=10,choices=category_choice,default='Cricket')
    votes = models.IntegerField(null=False,default=0)
    tot_votes = models.IntegerField(null=False,default=0)
    vote1 = models.IntegerField(null=False,default=0)
    vote2 = models.IntegerField(null=False,default=0)
    col_amt = models.IntegerField(null=False,default=0)
    userno = models.IntegerField(default=0)
    unit_value = models.IntegerField(default=0)


    def __str__(self):
        return self.matchId
    def get_absolute_url(self):
        return reverse("details",args=[self.matchId])


