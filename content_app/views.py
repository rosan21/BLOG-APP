from django.shortcuts import render
from content_app.models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})
