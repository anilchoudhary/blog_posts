from django.urls import re_path
from django.contrib import admin

app_name = "users-api"

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

urlpatterns = [
    re_path(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
