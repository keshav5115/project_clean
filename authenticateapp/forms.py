from django import forms
from .models import Autheregister
from django.contrib.auth.hashers import make_password

class Autheregform(forms.ModelForm):
    class Meta:
        model=Autheregister
        fields=['username','first_name','last_name','email','phone','gender','password']

    def save(self,commit=True):
        user=super().save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user