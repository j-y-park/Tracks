from django import forms
from django.forms import ModelForm
from TracksApp.models import *


class UploadFileForm(forms.Form):
    file  = forms.FileField()



class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['field1', 'field2', 'field3', 'field4']