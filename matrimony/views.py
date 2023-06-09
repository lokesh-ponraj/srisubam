from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'POST':
        emailAdd = request.POST.get('emailAdd')
        passWord = request.POST.get('passWord')
        user = authenticate(request, emailAdd=emailAdd, passWord=passWord)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            return render(request, 'matrimony/index.html',{messages.info('Invalid Credentials')})
    return render(request, 'matrimony/index.html')

def register(request):
    return render(request, 'matrimony/register.html')



def matching(request):
    return render(request, 'matrimony/matching.html')



def membership(request):
    return render(request, 'matrimony/membership.html')


def contact(request):
    return render(request, 'matrimony/contact.html')


def home(request):
    return render(request, 'matrimony/homePage.html')