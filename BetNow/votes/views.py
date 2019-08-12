from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponseRedirect
from creatematch.models import match
from django.contrib.auth.models import User
from Account.models import Userprofile
from .models import uservotes
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def usevote(request,matchId):
    current_match = get_object_or_404(match,matchId=matchId)
    usern = User.objects.get(username__exact=request.user)
    profile = get_object_or_404(Userprofile, user_id=usern.pk)
    ava_vote = int(profile.wallet/15)
    context = {'Id': matchId,
               'current_match':current_match,
               'ava_vote':ava_vote,
               'profile':profile,
               }
    if request.method == 'POST':
      selected_team = request.POST['d']
      selected_vote = request.POST['v']  # giving userid for model vote to login user
      if int(selected_vote) < int(ava_vote) and int(selected_vote) > 0:
         selected_vote = int(selected_vote)
         team1 = current_match.team1
         if selected_team == team1:
            current_match.vote1 += selected_vote
            uservotes.objects.create(mnumber=matchId, uname=request.user,teamone = selected_vote,vote=selected_vote,is_voted = True,team=selected_team)
         else:
            current_match.vote2 += selected_vote
            uservotes.objects.create(mnumber=matchId, uname=request.user, teamtwo=selected_vote,vote=selected_vote, is_voted=True,team=selected_team)
         current_match.tot_votes += selected_vote
         vote_value = selected_vote*15
         current_match.col_amt  = current_match.col_amt + vote_value
         current_match.userno  = current_match.userno + 1
         profile.wallet  = profile.wallet - vote_value
         profile.save()
         current_match.save()
         return HttpResponseRedirect(reverse('homepage'))
      else:
          messages.error(request, "Please vote between 0 to match votes")


    return render(request,'vote.html',context)
