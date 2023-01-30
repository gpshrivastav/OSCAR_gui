from django import forms

MODLE_LIST= [
    'EDGARv6',
    'ACCMIP',
    'CMIP6',
    ]

class ModelForm(forms.Form):
    model_name = forms.CharField(widget=forms.Select(choices=MODLE_LIST))

    