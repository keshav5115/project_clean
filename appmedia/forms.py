from appmedia.models import Blog
from django import forms

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'