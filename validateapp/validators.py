from django import forms
def namelength(name):
    if len(name)<5:
        raise forms.ValidationError('name should contain atleast 6 characters')
    return name
def firstletter(name):
    if name[0].islower():
        raise forms.ValidationError('first char should be capital letter')
    return name