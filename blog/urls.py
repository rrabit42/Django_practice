from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('<int:id>/', views.post_detail),
]
