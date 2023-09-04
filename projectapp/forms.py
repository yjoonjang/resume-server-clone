from django import forms
from django.forms import ModelForm

from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    # article = forms.inlineformset_factory(Project, Article, form=ArticleCreationForm, extra=1)
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'image']