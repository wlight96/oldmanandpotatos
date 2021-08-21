from django.urls import path 
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('<str:store_id>',views.store_page, name = 'storepage'),
]
