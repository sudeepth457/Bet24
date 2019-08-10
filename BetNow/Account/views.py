from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm,UserRegistration,userprofileform
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Userprofile
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
    return render(request,'home.html')




def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
               if user.is_active:
                   login(request, user)
                   return HttpResponseRedirect(reverse('homepage'))
               else:
                   return HttpResponse('User is not active')
            else:
                 return HttpResponse('user is none')
    else:
          form = UserForm()
    context={'form':form,}
    return render(request,'login.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        profileform = userprofileform(request.POST or None)
        if form.is_valid() and profileform.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('homepage'))
    else:
        form = UserRegistration()
        profileform = userprofileform()
    context ={
    'form' :form,
    'profileform':profileform,
    }
    return render(request,'register.html',context)

def User_logout(request):
    logout(request)
    return redirect('homepage')

def userprofile(request, user):
        usern = User.objects.get(username__exact=user)
        profile = get_object_or_404(Userprofile, user_id=usern.pk)
        context = {'profile': profile,
                   'user': usern
                   }
        return render(request, 'profile.html', context)

def walletrecharge(request,user):
    if request.method == 'POST':
        usern = User.objects.get(username__exact=user)
        profile = get_object_or_404(Userprofile, user_id=usern.pk)
        Value = 0
        Value = request.POST['q']
        Value = int(Value)
        profile.wallet  = profile.wallet + Value
        profile.save()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request,'payment.html')