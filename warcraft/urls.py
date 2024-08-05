from warcraft import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('screenshots/', views.screenshot, name='screenshot'),
    path('videos/', views.video, name='video'),
    path('musics/', views.music, name='music'),
    path('add/', views.add, name='add'),
    path('add-video/', views.add_video, name='add_video'),
    path('add-music/', views.add_music, name='add_music'),
    path('add-screenshot/', views.add_screenshot, name='add_screenshot'),
]