from django.urls import path
from . import views as law_views

urlpatterns = [
    path('', law_views.home, name='law-home'),
    path('about/', law_views.about, name='law-about'),
    path('community/', law_views.community, name='law-community'),
    path('events/', law_views.events, name='law-events'),
    path('gallery/', law_views.gallery, name='law-gallery'),
    path('projects/', law_views.projects, name='law-projects'),
    path('chat/', law_views.chat, name='law-chat'),
    path('login/', law_views.login, name='law-login'),
]
