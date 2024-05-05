from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('nh/', views.NotHomeView.as_view(), name='nh'),
]



