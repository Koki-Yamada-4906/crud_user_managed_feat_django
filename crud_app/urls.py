from django.contrib import admin
from django.urls import path
from . import views
from .views import user_list, user_detail, update_user, add_user, add_user2, delete_user

app_name = "app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_list, name="list"),  
    path("users/<int:pk>/", user_detail, name="user_detail"),
    path("update/<int:pk>", update_user, name="update"),
    path("add/" ,add_user, name="add"),
    path("add2/", add_user2, name="add2"),
    path("delete/<int:pk>", delete_user, name="delete"),
]