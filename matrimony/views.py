from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def check(request):
    return render(request, 'matrimony/template.html')

def new(request):
    return render(request, 'matrimony/new.html')