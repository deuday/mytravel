from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('register')
    return render(request, 'signin.html')


def security(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['conf_password']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "user already exists!")
                return redirect('security')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already registered")
                return redirect('security')
            else:
                user = User.objects.create_user(username=username, last_name=last_name, first_name=first_name,
                                                email=email,
                                                password=password)
            user.save();
            return redirect('register')
            print("user registered")
        else:
            messages.info(request, "incorrect password")
            return redirect('security')
        return redirect('/')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
