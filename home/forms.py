from django import forms
from .models import Product


class PostSearchForm(forms.Form):
	search = forms.CharField()