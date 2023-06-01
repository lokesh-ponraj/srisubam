from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'POST':
        emailAdd = request.POST.get('emailAdd')
        passWord = request.POST.get('passWord')
        user = authenticate(request, emailAdd=emailAdd, passWord=passWord)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return render(request, 'matrimony/home.html',{messages.info('Invalid Credentials')})
    return render(request, 'matrimony/home.html')

def register(request):
    return render(request, 'matrimony/register.html')



def membership(request):
    return render(request, 'matrimony/membership.html')