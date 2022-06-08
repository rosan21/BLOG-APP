from django.shortcuts import render,redirect
from authapp.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as django_logout

# Create your views here.

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'register.html', {'form':form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            fn = form.cleaned_data['first_name']
            ln = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            User.objects.create_user(first_name=fn,last_name=ln,username=username, email=email, password=password )

            return redirect('login')
        else:
            return render(request, 'register.html', {'form':form})


def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            next_url = request.GET.get('next')
            if next_url is None:
                return redirect('home')
            else:
                return redirect(next_url)

            
        else:
            return render(request, 'login.html',{'form':form})

def signout(request):
    django_logout(request)
    return redirect('login')
    



    
