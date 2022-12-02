from django.urls import path
from. import views

app_name='authe'

urlpatterns=[ 
    path('reg/',views.Authregview,name='reg/'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
]