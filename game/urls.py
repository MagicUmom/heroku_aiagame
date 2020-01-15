from django.urls import path, include

from . import views

app_name = 'game'

urlpatterns = [
    path( '', views.index, name='index'),
    path( 'controll_pannel/', views.controll_pannel, name='controll_pannel'),
    path( 'testing/' , views.testing_page, name='testing_page'),


    path( 'admin_api/game_over', views.admin_api_game_over, name='admin_api_game_over' ),
    path( 'admin_api/new_game',  views.admin_api_new_game,  name='admin_api_new_game' ),
    path( 'admin_api/confirm',   views.admin_api_confirm,   name='admin_api_confirm' ),
    path( 'admin_api/lock',      views.admin_api_lock,      name='admin_api_lock' ),

    path( 'palyer_api/betting_red',      views.player_api_betting_red,      name='player_api_betting_red' ),
    path( 'palyer_api/betting_white',    views.player_api_betting_white,    name='player_api_betting_white' ),
    path( 'palyer_api/update_odds',      views.player_api_update_odds,      name='player_api_update_odds' ),

    path( 'polling/apis',    views.polling_apis,  name='polling_apis'),
]
