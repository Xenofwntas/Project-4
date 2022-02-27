
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("profile/<str:user>/follow", views.follow, name="follow"),
    path("following/<str:user>", views.following, name="following"),
    path("like/<int:pk>", views.like, name="like"),
    path("edit/<int:pk>", views.edit, name="edit")
]
