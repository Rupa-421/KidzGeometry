from django import forms
from .models import Application
class uploadForm(forms.Form):
    file=forms.FileField()
class ApplicationForm(forms.ModelForm):
    des = forms.CharField(required=False, widget=forms.Textarea())
    class Meta:
        model=Application
        fields=('title','link','startdate','enddate')

