from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^method/', views.method, name='method'),
    url(r'^conclusion/', views.conclusion, name='conclusion'),
]