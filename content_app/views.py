from django.shortcuts import redirect, render
from content_app.models import Blog
from content_app.forms import BlogForm
from Blog import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def add_blog(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request,'add.html',{'form':form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            Blog.objects.create(title = title, content = content, user_id= request.user.id)
            
            return redirect('home')
        else:
            return render(request,'add.html', {'form': form})

def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('home')

def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'GET':
        form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'form':form})
    else:
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.content = form.cleaned_data['content']
            blog.save()
            return redirect('home')
        else:
            return render(request, 'edit.html', {'form':form})

