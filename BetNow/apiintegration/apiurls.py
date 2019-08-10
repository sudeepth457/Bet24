from rest_framework import routers
from .views import matches
from django.urls import path,include

router = routers.DefaultRouter()
router.register('',matches)

urlpatterns = [
    path('matches/',include(router.urls)),

    ]