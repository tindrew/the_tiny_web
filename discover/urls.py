from django.urls import path
from . import views

urlpatterns = [
    path('discover-articles/', views.discover_articles, name='discover-articles'),
    path('article/<int:article_id>/', views.discover_article_detail, name='discover-article-detail'),
]
