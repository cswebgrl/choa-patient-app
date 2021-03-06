from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^respond/(?P<form_id>[-\w]+)/$', views.respond, name='respond'),
    url(r'^respond_hh/', views.respond_hh, name='respond'),
    url(r'^respond_wic/', views.respond_wic, name='respond'),
    url(r'^respond_food/', views.respond_food, name='respond'),
    url(r'^respond_status/', views.respond_status, name='respond'),
    url(r'^about/', views.about, name='about'),
    url(r'^messages/', views.messages, name='messages'),
    url(r'^history/', views.history, name='history'),
    url(r'^response-details/(?P<responseid>[0-9a-f]*)/$', views.details, name='details')
]
