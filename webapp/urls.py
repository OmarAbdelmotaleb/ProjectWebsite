from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .views import UsersAPIView
# from .views import CurrentUserAPIView, LoginAPIView, update_clicks

urlpatterns = [
    path("", views.index, name="index"),
    path('users/', UsersAPIView.as_view(), name='users-create'), 
    path('users/<str:pk>/', UsersAPIView.as_view(), name='users-detail'),
]