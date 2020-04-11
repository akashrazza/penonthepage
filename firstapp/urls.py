from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<str:a>/',views.indexReq,name='index'),
    path('contact',views.contact,name='contact'),
    path('add',views.add,name='add'),
    path('single/<int:a>/',views.single,name='single'),
    path('single/<int:a>/comment',views.comment,name='comment'),
    path('about',views.about,name='about')
]