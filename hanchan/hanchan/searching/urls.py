from django.urls import path 
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('search_banchan/', views.banchan, name="banchan"),
    path('search_locate/',views.location, name = 'locate'),
]