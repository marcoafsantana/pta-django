from django import forms

from core.models import Posts

class PostForm(forms.ModelForm):
  class Meta:
    model = Posts
    fields = ['title', 'text']