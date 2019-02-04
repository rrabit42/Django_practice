from . import views
from django.urls import path, re_path

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile),
]