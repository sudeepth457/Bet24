from django.db import models
from creatematch.models import match
# Create your models here.
class resultsection(models.Model):
    match = models.CharField(max_length=50)
    team = models.CharField(default=0,max_length=500)

    def __str__(self):
        return self.match