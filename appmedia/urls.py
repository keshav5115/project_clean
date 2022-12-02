from django.urls import path
from . import views

app_name='appmedia'

urlpatterns=[ 
    path('blog/',views.Blogview,name='blog'),
    path('blogread/<pk>/',views.Blogread,name='blogread'),
    path('blogall/',views.Blogget,name='blogall'),
    path('blogupdate/<pk>/',views.Blogupdate,name='blogupdate'),
    path('blogdel/<pk>/',views.Blogdelete,name='blogdel')
]
