from os import name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Userpage
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['useremail']
        Bdate = request.POST['b_date']
        U_name = request.POST['name']
        phone_No = request.POST['phone']

        if User.objects.filter(username = username).exists():
            return render(request, 'signup.html', {'error' : "이미 존재하는 사용자 입니다." })
            
        if password == request.POST['passwordCheck']:
            user = User.objects.create_user(
                username, email, password = password
            )    
            Userpage.objects.create(
                userid = username,
                useremail = email,
                name = U_name,
                b_date = Bdate,
                user_phone = phone_No,
            ).save()
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request, 'signup.html',{'error' : "비밀번호가 일치하지 않습니다."})
    else :
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None :
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request, 'login.html', {'error': "사용자 이름 혹은 패스워드가 틀렸습니다."})
    else : 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
