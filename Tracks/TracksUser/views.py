from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from TracksUser.models import TracksUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def register(request):
    """Register a user."""
    pass

def signIn(request):
    """Custom login"""
    email = password = ''
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('')

    return render_to_response('login.html', {'email': email})
