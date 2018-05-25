from django import forms
from .models import News, Tags, Language


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','subtitle','content','publish_date','language','tags']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['name','language']