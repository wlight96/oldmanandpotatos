from django.shortcuts import redirect, render
from mainpage.models import Banchan
from account.models import Store,Userpage
from django.db import connection
# Create your views here.
def home(request):
    # 많이 팔리는 반찬 보여주기 HOW ? : 아직 판매가능 여부 구현안하여 sale하지 않는 품목 제시
    best_banchan_list = Banchan.objects.filter(saleflag = 1)[:4]
    # 최근 등록된 반찬 보여주기 
    new_banchan_list = Banchan.objects.all().order_by('-banchan_code')[:4]

    store_list = Store.objects.all()
    if request.method == "POST":
        banchan_name = request.POST['banchan']
        banchan_list= Banchan.objects.filter(banchan_name__contains = banchan_name)
        return render(request,'searching_banchan.html',{'banchan_list' : banchan_list, 'store_list' : store_list}) 
    else:
        if request.user.is_authenticated:
            username = request.user.username
            try : 
                userinfo = Userpage.objects.get(userid = username)
                addr = userinfo.address.split()
                store_list = Store.objects.filter(address__contains = addr[1]) 
                return render(request,'home.html', {'userinfo': userinfo, 'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
            except :
                userinfo = Store.objects.get(store_id = username)
                addr = userinfo.address.split()
                store_list = Store.objects.filter(address__contains = addr[1])
                return render(request,'home.html', {'userinfo': userinfo, 'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
                
        else:
            return render(request, 'home.html', {'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
    