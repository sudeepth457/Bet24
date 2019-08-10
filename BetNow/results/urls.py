from django.urls import path
from . import views

urlpatterns = [
    path(r'result/(?P<matchId>\w+)/$',views.results, name='result'),
    path(r'matchresult/(?P<matchId>\w+)/$',views.matchresult, name='mresult'),
]