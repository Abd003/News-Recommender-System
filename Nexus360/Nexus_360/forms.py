from django import forms
from .models import News_Post



class addArticleForm(forms.ModelForm):
    class Meta:
        model=News_Post

        fields=('title','News_content','date','author')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'News_content': forms.Textarea(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
        }

class updateArticleForm(forms.ModelForm):
    class Meta:
        model=News_Post

        fields=('title','News_content')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'News_content': forms.Textarea(attrs={'class':'form-control'}),

        }
