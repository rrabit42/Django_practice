from . import views
from django.urls import path, re_path

urlpatterns = [
    path('profile/', views.profile),
]