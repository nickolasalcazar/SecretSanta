from django.urls import path
from . import views

from .views import (
	GameListView,
	GameDetailView,
	GameDeleteView
)

urlpatterns = [
    path('', views.home, name='game-home'),

    #path('create/', GameCreateView.as_view(), name='game-create'),	# Class-based
    path('create/', views.createGame, name='game-create'),			# Function-based

    # Is the extra "game/" at the beginning of each URL redundant?
    # Remove and test to see if it can be removed.
    path('game/view-games/', GameListView.as_view(), name='view-games'),

    path('game/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    
    # Function-based view
    # Change 'name' to more descriptive?
    path('game/<int:pk>/update/', views.updateGame, name='game-update'), 

    # Delete view
    path('game/<int:pk>/delete/', GameDeleteView.as_view(), name='game-delete'),

]