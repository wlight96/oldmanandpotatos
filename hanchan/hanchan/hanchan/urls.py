from django.contrib import admin
from django.urls import path, include
import mainpage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainpage.views.home, name = "home"),
    path('mainpage/',include('mainpage.urls')),
    path('account/',include('account.urls')),
    path('searching/',include('searching.urls')),
    path('store/',include('store.urls')),
]
