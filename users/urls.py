from collections import UserList
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('getusers/', views.UserList.as_view(), name='user_list'),
    path('getusers/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]