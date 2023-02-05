from django.urls import path

from .views import CreateUser,UserList
urlpatterns = [
    path("users", CreateUser.as_view()),
    path("api/users",UserList.as_view()),
   
   
]