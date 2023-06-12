from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    #path('listofusers',views.listofusers,name='listofusers'),
    path('follow',views.follow,name='follow'),
    path('unfollow',views.unfollow,name='unfollow'),
    path('fers',views.fers,name='fers'),
    path('fings',views.fings,name='fings'),
    path('explore',views.explore,name='explore'),
    path('addtweet',views.addtweet,name='addtweet'),
    path('pagevisit',views.pagevisit,name='pagevisit')
]