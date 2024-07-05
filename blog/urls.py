from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('dashboard/post', views.dashboard_post, name='dashboard_post'),
    path('dashboard/post/new', views.dashboard_post_new, name='dashboard_post_new'),
    path('dashboard/post/view/<str:slug>', views.dashboard_post_view, name='dashboard_post_view'),
    path('post/<str:slug>', views.single_post, name='single_post'),
]
