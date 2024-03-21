from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib import auth
# Create your views here.
from golos.form import UserAuth
from golos.models import Candidat

def index(request):
    if request.POST:
        if request.user.is_voted != True:
            vote_id = request.POST['candidat']
            candidat = Candidat.objects.filter(id = vote_id).last()
            candidat.votes += 1
            candidat.save()
            request.user.is_voted = True
            request.user.save()

    context = {
        "user" : request.user,
        "candidats" : Candidat.objects.all()
        }
    return render(request,'golos/index.html', context)

def login(request):
    if request.method == "POST":
        form = UserAuth(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('golos:index'))
    else:
        form = UserAuth()
    context = {'form': form,
               "user" : request.user,
               'title': "Авторизация в СДГ"}
    return render(request, "golos/login.html", context)

def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('golos:index'))