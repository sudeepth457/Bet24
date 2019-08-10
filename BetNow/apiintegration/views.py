from django.shortcuts import render
from .serializers import Matchserializers
# Create your views here.
from rest_framework import viewsets
from creatematch.models import match
import requests



class matches(viewsets.ModelViewSet):
    queryset = match.objects.all()
    serializer_class = Matchserializers


def home(request):
    response = requests.get('http://127.0.0.1:1144/employees/?format=json')
    empdata = response.json()
    print(empdata)
    for i in empdata:
       print(i['firstname'])
    return render(request, 'core.html',
    )