# Create your views here.
from django import forms
from TracksApp_forms import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.core.urlresolvers import reverse
from TracksApp.models import *
import os
from django.utils import timezone
import sys
import traceback


def index(request):
    form = UploadFileForm()
    return render(request, 'TracksApp/index.html', {'form': form})


def userprofile(request):
    temp_user = User.objects.get(username="test") #temporary line. FOR TESTING ONLY

    if(User.has_userprofile(temp_user)):
        temp_instance = temp_user.userprofile
    else:
        temp_instance = UserProfile(user=temp_user)

    if (request.method == 'POST'):
        form = UserProfileForm(request.POST, instance=temp_instance)
        if(form.is_valid):
            try:
                form.save()
                return HttpResponseRedirect('TracksApp/userprofile.html');
            except:
                response = HttpResponse(traceback.format_exc()) # Currently sends a response with the traceback of the error. DO NOT USE IN PRODUCTION.
                response.status_code = 500;
                return response
        else:
            response = HttpResponse('form not valid')
            response.status_code = 400;
            return response

    else:
        form = UserProfileForm(instance=temp_instance)
        return render(request, 'TracksApp/userprofile.html', {'form' : form})


def upload_MP3(request):
    #print('entered uploadmp3')
    if (request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES)
        if (form.is_valid):
            try:
                temp_mp3 = request.FILES['file']
                new_track = Track(filename=temp_mp3.name)
                handle_upload_file(temp_mp3, new_track)
                response = HttpResponse('success')
                response.status_code = 200;
                return response
            except:
                response = HttpResponse(traceback.format_exc()) # Currently sends a response with the traceback of the error. DO NOT USE IN PRODUCTION.
                response.status_code = 500;
                return response
        else:
            response = HttpResponse('form not valid')
            response.status_code = 400;
            return response
    else:
        response = HttpResponse('method not post')
        response.status_code = 400;
        return response


