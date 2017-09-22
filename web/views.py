from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponseRedirect("/login/")
