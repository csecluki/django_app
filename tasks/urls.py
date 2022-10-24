from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_home_view, name='task_home'),
    path('add/', views.task_add_view, name='task_add'),
    path('<slug:slug>/edit/', views.task_modify_view, name='task_modify'),
    path('<slug:slug>/remove/', views.task_remove_view, name='task_remove'),
    path('<slug:slug>/change-status/', views.task_change_status_view, name='task_change_status'),
]
