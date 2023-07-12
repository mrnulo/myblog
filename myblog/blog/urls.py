from django.urls import path
from .views import register, login_view, logout_view, home, create_post, edit_post, delete_post

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:pk>/', edit_post , name='edit_post'),
    path('delete/<int:pk>/', delete_post , name='delete_post'),
    path('accounts/login/', login_view, name='login'),
]

