from django import forms

from validateapp.models import library

class libraryform(forms.ModelForm):
    class Meta:
        model=library
        fields='__all__'
        widgets={'bookid':forms.TextInput(attrs={'placeholder':'enter book id'}),
                 'bname':forms.TextInput(attrs={'placeholder':'enter book name'}),
                 'author':forms.TextInput(attrs={'placeholder':'enter author name'}),
                 'price':forms.NumberInput(attrs={'placeholder':'enter book price'}),
                 'edition':forms.TextInput(attrs={'placeholder':'enter book edition'}),}
    

    # def clean_bname(self):
    #     name=self.cleaned_data['bname']
    #     if len(name)<=5:
    #         raise forms.ValidationError('book name should contain atleast 6 character')
    #     return name
    
    # def clean_author(self):
    #     author=self.cleaned_data['author']
    #     author=author.title()
    #     if len(author)<5:
    #         raise forms.ValidationError('author name should contain atleast 5 characters')
    #     return 'Mr. '+ author
    # def clean_price(self):
    #     price=self.cleaned_data['price']
    #     if price <= 1000:
    #         raise forms.ValidationError('price should more than 1000 rupees ')
    #     return price

    # def clean_edition(self):
    #     edition=self.cleaned_data['edition']
    #     return edition