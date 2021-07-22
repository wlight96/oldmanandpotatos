from os import execlpe
from django.core import exceptions
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from .models import Userpage,Store,Allergy
from mainpage.models import Banchan
import random
import string

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['useremail']
        Bdate = request.POST['b_date']
        U_name = request.POST['name']
        addr = request.POST['address']
        zip = request.POST['zipcode']
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
                zipcode = zip,
                address = addr
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

def mypage(request, username):
    store_flag = 0
    if request.method == "POST" and store_flag == 1:
        banchan_code = request.POST['banchan_code']
    try :
        userinfo = Userpage.objects.get(userid = username)
        return render(request, 'mypage.html', {'userinfo': userinfo,
        'store_flag' : store_flag})
    except :
        userinfo = Store.objects.get(store_id = username)
        banchan_list = Banchan.objects.filter(s_id = username)
        store_flag = 1
        return render(request, 'mypage.html', {'userinfo': userinfo,
        'store_flag' : store_flag,
        'banchan_list': banchan_list})

    #likebanchan = like_banchan.objects.get(userid = user=name)

def store_signup(request):
    if request.method == "POST":
        store_id = request.POST['username']
        password = request.POST['password']
        email = request.POST['useremail']
        store_name = request.POST['storename']
        zipcode = request.POST['zipcode']
        addr = request.POST['address']
        addr_detail = request.POST['address_detail']
        extra_addr = request.POST['extra_address']
        phone_No = request.POST['store_phone']

        if User.objects.filter(username = store_id).exists():
            return render(request, 'store_signup.html', {'error' : "이미 존재하는 사용자 입니다." })
            
        if password == request.POST['passwordCheck']:
            user = User.objects.create_user(
                store_id, email, password = password
            )    
            Store.objects.create(
                store_id = store_id,
                store_name = store_name,
                zipcode = zipcode,
                adress = addr,
                address_detail = addr_detail,
                extra_address = extra_addr,
                store_phone = phone_No,
            ).save()
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request, 'store_signup.html',{'error' : "비밀번호가 일치하지 않습니다."})
    else :
        return render(request, 'store_signup.html')



def add_banchan(request):
    if request.method == "POST":
        banchan_name = request.POST['banchan_name']
        banchan_category = request.POST['banchan_category']
        banchan_cost = request.POST['banchan_cost']
        username = request.POST['username']
        banchan_img = request.POST['banchan_img']
        if Banchan.objects.filter(banchan_name = banchan_name).exists():
            return render(request, 'store_signup.html', {'error' : "이미 등록된 반찬 입니다." })
        else :    
            Banchan.objects.create(
                s_id = username,
                banchan_name = banchan_name,
                category = banchan_category,
                saleflag = 1,
                discount = 0,
                cost = banchan_cost,
                banchan_img = banchan_img,
                banchan_code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
            ).save()
            return redirect('/')
    else :
        return render(request, 'add_banchan.html')
