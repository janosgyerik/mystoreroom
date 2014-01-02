from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as django_logout
from django.template import RequestContext


def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))


def logout(request):
    django_logout(request)
    return redirect('home')

