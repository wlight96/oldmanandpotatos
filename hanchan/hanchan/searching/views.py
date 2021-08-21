from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from mainpage.models import Banchan
from account.models import Store

# Create your views here.
def banchan(request):
    if request.method == "POST":
        banchan_name = request.POST['banchan']
        banchan_list= Banchan.objects.filter(banchan_name__contains = banchan_name)

        return render(request,'searching_banchan.html',{'banchan_list' : banchan_list}) 
    else:
        return render(request,'searching_banchan.html')


def location(request):
    
    return render(request,'searching_location.html')