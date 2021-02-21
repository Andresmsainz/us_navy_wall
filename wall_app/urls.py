from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('stations/new',views.newstation),
    path('create_station',views.create_station),
    path('new_assign_station/<int:station_id>',views.new_assign_station),
    path('assign_station/<int:station_id>',views.assign_station),
    path('history_match/<int:history_id>/<int:station_id>',views.history_match),
]
