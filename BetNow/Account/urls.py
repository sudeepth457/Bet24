from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.user_login,name="login"),
    path('signup/',views.register,name="Signup"),
    path('logout/',views.User_logout,name='Logout'),
    path(r'Profile/(?P<user>\w+)/$',views.userprofile, name='profile'),
    path(r'Payment/(?P<user>\w+)/$',views.walletrecharge, name='recharge'),
]