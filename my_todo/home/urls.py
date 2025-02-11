from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_todos, name='home'),
    path('crsasdeate/', views.create_todo, name='abc'),
    path('complete/<int:id>/', views.complete_todo, name='complete'),
    path('delete/<int:id>/', views.delete_todo, name='delete'),
    path('update/<int:id>/', views.update_todo, name='update'),
]