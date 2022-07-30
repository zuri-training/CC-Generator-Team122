from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def home_view(request):
    return render(request, 'home.html')
# def explore(request):
#     return HttpResponse("EXPLORE")
# def signup_view(request):
#     return render(request, 'signup.html')
def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    accounts_user = request.user
    print(accounts_user)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        # lname = request.POST.get('lname', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        rt_password = request.POST.get('rpassword', None)
        profilepic = request.POST.get('profilepic', None)
        if password != rt_password:
            messages.error(request, messages.INFO, "Password Incorrect")
        user = User.objects.create_user(username= username, email= email, password= password)
        user.save()
        return redirect('accounts:login')
    return render(request, 'signup.html')