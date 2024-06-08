from django import forms

class ClassifyForm(forms.Form):
    subject = forms.CharField(max_length = 200, help_text='Enter Subject of Email')

class SummariseForm(forms.Form):
    content= forms.CharField(max_length=300, min_length=75, help_text='Enter Content')