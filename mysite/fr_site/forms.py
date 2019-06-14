from django import forms

class FeaturesForm(forms.Form):
	title = forms.CharField(label='Title', max_length=60)
	#Interesting, there is no textfield in django forms
	#https://stackoverflow.com/questions/7302889/textfield-missing-in-django-forms
	description = forms.CharField(widget=forms.Textarea)