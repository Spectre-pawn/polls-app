from django.urls import path,include
from . import views

urlpatterns = [
 
    path('',views.index,name='index' ),
    path('mypolls',views.mypolls,name='mypolls'),
    path('profile',views.profile,name='profile'),
    path('create',views.createpoll,name='createpoll'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('vote/<poll_id>/',views.vote,name='vote'),
    path('results/<poll_id>/', views.results, name='results'), 
]