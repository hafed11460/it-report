# from rapport.models import Rapport
from django.forms import fields
from rapport.models import Rapport
from django import forms
# from category.models import Category


class RapportForm(forms.ModelForm):
    class Meta:
        model=Rapport
        fields = ['title','date','starthour','endhour', 'description','equipment','state_befor','state_after','device_used','type_di','n_di','note']
        widgets = {
        'title': forms.TextInput( attrs={'class':'form-control', 'placeholder':'Title'}),
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'starthour': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'Start Hour', 'type':'time'}),
        'endhour': forms.TimeInput(attrs={'class':'form-control', 'placeholder':'End Hour', 'type':'time'}),

        'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description', 'rows':4}),
        'equipment': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Equipment', 'rows':4}),

        'state_befor': forms.Textarea(attrs={'class':'form-control', 'placeholder':'state befor', 'rows':4}),
        'state_after': forms.Textarea(attrs={'class':'form-control', 'placeholder':'state after', 'rows':4}),

        'type_di': forms.Select(attrs={'class':'form-control', 'placeholder':'Type DI '}),
        'n_di': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° DI'}),


        'device_used': forms.Textarea(attrs={'class':'form-control', 'placeholder':'device used', 'rows':4}),
        'note': forms.Textarea(attrs={'class':'form-control', 'placeholder':'note', 'rows':4}),
    }