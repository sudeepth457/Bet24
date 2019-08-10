from django.urls import path
from . import views

urlpatterns = [
    path(r'matches/(?P<category>\w+)/$',views.matchlists, name='list'),
    path(r'match details/(?P<id>\d+)/$',views.matchdetail, name='details'),
    path('Search/', views.search, name='search'),

]