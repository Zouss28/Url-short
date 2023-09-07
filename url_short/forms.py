from django import forms

class ShortenURLForm(forms.Form):
    url = forms.URLField(label='Enter URL', widget=forms.TextInput(attrs={'placeholder': 'Enter URL'}))
