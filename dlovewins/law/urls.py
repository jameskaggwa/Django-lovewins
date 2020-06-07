from django.urls import path
from . import views as law_views

urlpatterns = [
    path('', views.home, name='law-home'),
    path('about/', views.about, name='law-about'),
    path('community/', views.community, name='law-community'),
    path('events/', views.events, name='law-events'),
    path('gallery/', views.gallery, name='law-gallery'),
    path('projects/', views.projects, name='law-projects'),
    path('chat/', views.chat, name='law-chat'),
    path('register/', views.register, name='law-register'),
    # path('login2/', law_views.login, name='law-login'),
]
