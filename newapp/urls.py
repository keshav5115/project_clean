from django.urls import path
from . import views
urlpatterns=[ 
    path('reg/',views.newuserview,name='reg'),
    path('login/',views.newlogin_view,name='login'),
    path('logout/',views.newlogout_view,name='logout'),
    path('home/',views.home,name='home'),

]