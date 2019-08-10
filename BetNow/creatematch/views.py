from django.shortcuts import render,get_object_or_404,reverse
from django.db.models import Q
from .models import match
from votes.models import uservotes
from results.models import resultsection
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def matchlists(request,category):
    details = match.objects.filter(
        Q(category__icontains=category))
    context={'details': details,
    }

    return render(request,'list.html',context)

def matchdetail(request,id):
    post =get_object_or_404(match,matchId=id)
    try:
     view = uservotes.objects.get(uname = request.user,mnumber = id)
    except uservotes.DoesNotExist:
     view = False
    try:
         result = resultsection.objects.get(match=id)
    except resultsection.DoesNotExist:
         result = False
    context = {'post' : post,
               'view' : view,
               'result': result,
            }
    return render(request,'detail.html',context)

def search(request):
    if request.method == 'POST':
        id=request.POST['search']
        if id:
            m =match.objects.filter(
        Q(team1__icontains=id)|Q(team2__icontains=id))
            if m :
                return render(request,'search.html',{'data':m})
            else:
                messages.error(request, "Ooops!!!! Please search again with approx. team name")


        else:
            return redirect('search')
    return render(request,'search.html')
