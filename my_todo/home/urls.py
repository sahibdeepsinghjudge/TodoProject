from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_todos, name='home'),
    path('crsasdeate/', views.create_todo, name='abc'),
]