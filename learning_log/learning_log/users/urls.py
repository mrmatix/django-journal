"""Defines url patterns for users."""

from django.contrib.auth import login
from django.urls import path, include
from django.contrib import admin
# from django.contrib.auth.views import LoginView

# from . import views

# app_name = 'users'
# urlpatterns = [
#     # Login page.
#     path('login/',
#          LoginView.as_view(template_name='users/login.html'), name="login"),
# ]
app_name = 'users'
urlpatterns = [
    # adding users
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
    # Login page.
    path('login/', login, {'template_name': 'users/login.html'},
         name='login'),
]
