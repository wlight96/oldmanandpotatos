from django.shortcuts import redirect, render
from mainpage.models import Banchan
from account.models import Store,Userpage
# Create your views here.
def home(request):
    if request.method == "POST":
        banchan_name = request.POST['banchan']
        banchan_list= Banchan.objects.filter(banchan_name__contains = banchan_name)
        return render(request,'searching_banchan.html',{'banchan_list' : banchan_list}) 
    else:
        if request.user.is_authenticated:
            username = request.user.username
            try : 
                userinfo = Userpage.objects.get(userid = username)
                return render(request,'home.html', {'userinfo': userinfo})
            except :
                userinfo = Store.objects.get(store_id = username)
                return render(request,'home.html', {'userinfo': userinfo})
                
        else:
            return render(request, 'home.html')
    