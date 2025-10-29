from django.contrib import admin
from django.urls import path
from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('place1/', views.place1, name='place1'),
    path('place2/', views.place2, name='place2'),
    path('place3/', views.place3, name='place3'),
    path('place4/', views.place4, name='place4'),
    path('place5/', views.place5, name='place5'),
]
