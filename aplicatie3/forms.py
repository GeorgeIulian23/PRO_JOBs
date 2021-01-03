from django import forms
from django.forms import TextInput, Select

from aplicatie3.models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['name',  'url', 'titlu', 'description','how_to_apply']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Numele Persoanei', 'class': 'form-control'}),
            'titlu': Select(attrs={'class': 'form-control'}),
            'description':TextInput(attrs={'class': 'form-control'}),
            'how_to_apply':TextInput(attrs={'cum sa aplici': 'Website', 'class': 'form-control'}),
            'url':TextInput(attrs={'placeholder': 'Site_web', 'class': 'form-control'}),

        }