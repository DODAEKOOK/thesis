from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.sub_intro, name='sub_intro'),
    url(r'^sb1/', views.sub1, name='sub1'),
    url(r'^sb2/', views.sub2, name='sub2'),
    url(r'^sb3/', views.sub3, name='sub3'),
    url(r'^sb4/', views.sub4, name='sub4'),
]