from content_app.models import Blog
from django.forms import ModelForm

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','user']