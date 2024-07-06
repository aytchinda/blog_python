from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('dashboard/post', views.dashboard_post, name='dashboard_post'),
    path('dashboard/post/new', views.dashboard_post_new, name='dashboard_post_new'),
    path('dashboard/post/view/<str:slug>', views.dashboard_post_view, name='dashboard_post_view'),
    path('dashboard/post/edit/<str:slug>', views.dashboard_post_edit, name='dashboard_post_edit'),
    path('post/<str:slug>', views.single_post, name='single_post'),
]

#J'aoute la configuration pour servir les fichier statiques pendant le developpement
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)