from django.urls import path
from . import views

urlpatterns = [
    path(r'vote/(?P<matchId>\w+)/$',views.usevote, name='vote'),
]