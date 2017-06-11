from django import forms
from .models import Theme, Content


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['text']
        labels = {'text': ''}


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
