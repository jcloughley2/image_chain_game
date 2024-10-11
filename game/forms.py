from django import forms

class DescriptionForm(forms.Form):
    description = forms.CharField(label='Describe the image', widget=forms.Textarea)
