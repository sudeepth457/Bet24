from django.shortcuts import render,get_object_or_404,reverse
from .models import resultsection
from votes.models import uservotes
from creatematch.models import match
from .forms import resultform
# Create your views here.
from django.http import HttpResponseRedirect
from Account.models import Userprofile
from django.db.models import Q
from django.contrib.auth.models import User

def results(request,matchId):
    post = get_object_or_404(resultsection, match=matchId)
    try:
       voted = uservotes.objects.get(uname = request.user,mnumber = matchId)
    except uservotes.DoesNotExist:
       voted = False
    match_details = get_object_or_404(match, matchId=matchId)
    context ={
        'post':post,
        'voted':voted,
        'match_details':match_details,
    }
    return render(request, 'result.html',context)



def matchresult(request,matchId):
    post = get_object_or_404(match, matchId=matchId)
    context = {
        'matchId': matchId,
        'post': post,
    }
    if request.method == 'POST':
        selected_team = request.POST['d']
        if post.team1 == selected_team :
            unit_value = (post.col_amt / post.vote1)
        else:
            unit_value = (post.col_amt / post.vote2)
        print(unit_value)
        post.unit_value = unit_value
        post.save()
        user_list = uservotes.objects.filter(mnumber__icontains=matchId)
        for user in user_list:
            if selected_team == user.team:
                moneycoll = int(user.vote) * unit_value
                user.money = moneycoll
                usern = User.objects.get(username__exact=user)
                profile = get_object_or_404(Userprofile, user_id=usern.pk)
                profile.wallet = profile.wallet + moneycoll
                profile.save()
                user.save()
                resultsection.objects.create(match=matchId,team=selected_team)
        return HttpResponseRedirect(reverse('homepage'))
    else:
        form = resultform()
    return render(request, 'matchresult.html',context)

