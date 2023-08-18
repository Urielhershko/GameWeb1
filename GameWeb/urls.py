from django.urls import path
from GameWeb import views

urlpatterns = [
   path('', views.games , name = "game-view"),
   path('login/', views.signin , name = "login"),
   path('logout/', views.logout_user , name = "logout"),
   path('register/', views.register, name='register'),
   path('home/', views.home , name = "home"),
   path('game/', views.games_text , name = "game-text"),
   path('place_order/<int:game_id>/', views.place_order, name='place-order')
]