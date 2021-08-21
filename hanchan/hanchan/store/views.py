from os import execlpe
from django.core import exceptions
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from account.models import Userpage, Store, Allergy
from mainpage.models import Banchan, BanchanIngredients

# Create your views here.
def store_page(request, store_id):
     store_info = Store.objects.get(store_id = store_id)
     banchan_list = Banchan.objects.filter(s_id = store_id)
     b_ingredient_list = []
     for banchan in banchan_list :
          b_ingredient_list+=BanchanIngredients.objects.filter(b_code = banchan.banchan_code)
     return render(request, 'storepage.html', {'store_info' : store_info, 'banchan_list' : banchan_list, 'b_ingredient_list' : b_ingredient_list})