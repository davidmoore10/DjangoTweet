from django.urls import path
from . import views

urlpatterns = [
    # path('',views.twitter_login)
    path('',views.home, name='home'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('tweet/', views.tweet, name='tweet'),
    path('failure/', views.failure, name='failure'),
    path('logout/', views.logout, name='logout'),
]