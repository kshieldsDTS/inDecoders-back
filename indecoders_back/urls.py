from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('LFWork/', views.LFWorkList.as_view(), name='LFWork_list'),
    path('LFWork/<int:pk>', views.LFWorkDetail.as_view(), name='LFWork_detail'),
    path('LFHelp/', views.LFHelpList.as_view(), name='LFHelp_list'),
    path('LFHelp/<int:pk>', views.LFHelpDetail.as_view(), name='LFHelp_detail')
]