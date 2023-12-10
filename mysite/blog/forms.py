from django import forms
from .models import Post
from ckeditor.fields import RichTextField

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'categories','image', 'status']
        widgets = {
            'content': RichTextField(),  # Use RichTextField for the 'content' field
        }
