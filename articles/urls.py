from django.urls import path

from . import views

urlpatterns = [
    path('', views.article_home_view, name='article_home'),
    path('add/', views.article_add_view, name='article_add'),
    path('<slug:slug>/', views.article_detail_view, name='article_detail'),
    path('<slug:slug>/edit/', views.article_edit_view, name='article_edit'),
    path('<slug:slug>/like/', views.article_like_view, name='article_like'),
    path('<slug:slug>/publish/', views.article_publish_view, name='article_publish'),
]
