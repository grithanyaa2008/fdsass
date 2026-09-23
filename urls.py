from django.urls import path
from . import views


urlpatterns = [

    path("", views.home, name="home"),
    path(
    "register/",
    views.register,
    name="register"
),

path(
    "login/",
    views.user_login,
    name="login"
),
path(
    "logout/",
    views.user_logout,
    name="logout"
),
    path(
        "complete/<int:task_id>/",
        views.complete_task,
        name="complete"
    ),

    path(
        "delete/<int:task_id>/",
        views.delete_task,
        name="delete"
    ),

    path(
        "edit/<int:task_id>/",
        views.edit_task,
        name="edit"
    ),

]