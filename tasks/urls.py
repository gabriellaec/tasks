from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.get, name='get'),
    path('new_task/', views.post, name='post'),
]
