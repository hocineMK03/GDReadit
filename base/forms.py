from django import forms

from .models import Place

class Placeform(forms.ModelForm):
    class Meta:

        model=Place
        
        fields=[
            'name','desc'
        ]


class placeformhtml(forms.Form):
    name=forms.CharField()
widget=forms.Textarea(
        
        attrs={
        "placeholder":"your name"
        }
)

    