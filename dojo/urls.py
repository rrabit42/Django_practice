from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    #\d나 /가 1번 이상 반복되면 함수 호출
    re_path('hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/', views.hello),
]