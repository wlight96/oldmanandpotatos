from django.shortcuts import redirect, render
from mainpage.models import Banchan
from account.models import Store,Userpage
# Create your views here.
def home(request):
    
    # 많이 팔리는 반찬 보여주기 HOW ? : 아직 판매가능 여부 구현안하여 sale하지 않는 품목 제시
    best_banchan_list = Banchan.objects.filter(saleflag = 1)[:4]
    # 최근 등록된 반찬 보여주기 
    new_banchan_list = Banchan.objects.all().order_by('-banchan_code')[:4]
    store_list = Store.objects.all()
    # 검색 후 
    if request.method == "POST":
        search_word = request.POST['keyword']
        search_menu = request.POST['search_menu']
        if search_menu == "반찬검색":
            banchan_list= Banchan.objects.filter(banchan_name__contains = search_word)
            return render(request,'searching_banchan.html',{'banchan_list' : banchan_list, 'store_list' : store_list}) 
        elif search_menu == "가게검색":
            banchan_list= Banchan.objects.filter(banchan_name__contains = search_word)
            return render(request,'storepage.html',{'banchan_list' : banchan_list, 'store_list' : store_list}) 
    # 검색 이전 
    else:
        if request.user.is_authenticated:
            username = request.user.username
            try : 
                userinfo = Userpage.objects.get(userid = username)
                addr = userinfo.address.split()
                store_list = Store.objects.filter(address__contains = addr[1]) 
                store_count = len(store_list)
                
                # 근처에 반찬 가게가 없을 경우
                if store_count == 0 :
                    store_list = Store.objects.filter(address__contains = addr[0])
                    store_count = len(store_list)
                # 가게가 있을 시 가게에 등록된 반찬 보여주기
                else :
                    new_banchan_list = []
                    for store in store_list :
                        new_banchan_list += (Banchan.objects.filter(s_id = store.store_id).order_by('-banchan_code')[:2])

                return render(request,'home.html', {'userinfo': userinfo, 'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
            # 반찬가게로 로그인 하였을 때, main page return 값 
            except :
                userinfo = Store.objects.get(store_id = username)
                addr = userinfo.address.split()
                store_list = Store.objects.filter(address__contains = addr[1])
                return render(request,'home.html', {'userinfo': userinfo, 'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
        else:
            return render(request, 'home.html', {'store_list' : store_list, 'b_list' : best_banchan_list, 'n_list' : new_banchan_list})
    