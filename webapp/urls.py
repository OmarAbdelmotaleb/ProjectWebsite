from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
# from .views import UsersAPIView, CurrentUserAPIView, LoginAPIView
from .views import CurrentUserAPIView, LoginAPIView, update_clicks

urlpatterns = [
    path("", views.index, name="index"),
    # path('users/', UsersAPIView.as_view(), name='users-create'), 
    # path('users/<int:pk>/', UsersAPIView.as_view(), name='users-detail'),
    # path('users/<int:pk>/', UsersAPIView.as_view(), name='users-detail'),
    path('update-clicks/', update_clicks, name='update-clicks'),
    path('users/me/', CurrentUserAPIView.as_view(), name='current-user'),
    path('login/', LoginAPIView.as_view(), name='login'),

]