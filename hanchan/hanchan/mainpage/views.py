from django.shortcuts import redirect, render
from mainpage.models import Banchan
from account.models import Store

# Create your views here.
def home(request):
    if request.method == "POST":
        banchan_name = request.POST['banchan']
        banchan_list= Banchan.objects.filter(banchan_name__contains = banchan_name)
        return render(request,'searching_banchan.html',{'banchan_list' : banchan_list}) 
    else:
        return render(request, 'home.html')
    