from django.urls import path

from . import views

urlpatterns = [
    # ex: /api/
    path('', views.index, name='index'),
    # ex: /api/users
    path('users/', views.get_all_users),
    # ex: /api/games
    path('games/', views.get_all_games, name='games'),
    # ex: /api/5/
    path('games/<int:game_id>/', views.game, name='game'),
    # ex: /api/5/results/
    path('games/<int:game_id>/players/', views.players, name='players'),
    # ex: /api/5/vote/
    path('games/<int:game_id>/actions/', views.actions, name='actions'),
]