from django.urls import path
from . import views

from .views import (
	GameCreateView,
)

urlpatterns = [
    path('', views.home, name='game-home'),

    path('create/', GameCreateView.as_view(), name='game-create'),

]