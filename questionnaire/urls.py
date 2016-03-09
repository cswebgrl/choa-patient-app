from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^respond/', views.questionnaire, name='questionnaire'),
    url(r'^about/', views.about, name='about'),
]