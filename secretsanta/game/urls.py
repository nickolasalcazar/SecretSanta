from django.urls import path
from . import views

from .views import (
	GameCreateView,
)

urlpatterns = [
    path('', views.home, name='game-home'),

    # Class-based view implementation
    #path('create/', GameCreateView.as_view(), name='game-create'),

    # Function based view implementation
    path('create/', views.createGame, name='game-create')

]