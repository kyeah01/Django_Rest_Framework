from django.urls import path
from . import views

urlpatterns = [
    path('musics/<int:music_pk>/', views.music_detail),
    path('musics/',views.music_list)
]