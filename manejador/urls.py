from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soapsl', views.soapsl, name='soapsl'),
    path('soapsl2', views.soapsl2, name='soapsl2'),
    path('<int:q_id>/', views.show, name='show'),
]
