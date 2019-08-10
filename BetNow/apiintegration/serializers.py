from rest_framework import  serializers
from creatematch.models import *

class Matchserializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = match
        fields = ('team1',
                  'team2',
                  'stadium',
                  'city',
                  'time',
                  'matchId',
                  'category',
                  'votes',
                  'url',
                  )