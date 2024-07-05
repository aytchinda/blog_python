from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('dashboard/post', views.dashboard_post, name='dashboard_post'),
    path('post/<str:slug>', views.single_post, name='single_post'),
]
