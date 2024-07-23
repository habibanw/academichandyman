from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/user/profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('providers:home')
    else:
        return render(request, 'users/user/register.html')


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS, 'Login successful')
        return redirect('providers:services')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid credentials')
        return redirect('providers:home')


def logout_user(request):
    request.session.flush()
    return redirect('providers:home')
