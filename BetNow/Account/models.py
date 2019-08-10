from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
      user = models.OneToOneField(User,on_delete=models.CASCADE)
      phone =models.CharField(max_length=10,null=False)
      wallet = models.IntegerField(default=0)
      wins = models.IntegerField(default=0)
      losses =models.IntegerField(default=0)
      money_earned = models.IntegerField(default=0)
      country = models.CharField(max_length=500)

      def __str__(self):
          return self.user.username