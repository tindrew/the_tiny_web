from django.urls import path
from . import views

urlpatterns = [
    # path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('create-article/', views.create_article, name='create-article'),
    path('user-articles/', views.user_articles, name='user-articles'),
    path('update-article/<str:pk>', views.update_article, name='update-article'),
    path('delete-article/<str:pk>', views.delete_article, name='delete-article'),
    path('account-management/', views.account_management, name='account-management'),
    path('delete-account/', views.delete_account, name='delete-account'),

]