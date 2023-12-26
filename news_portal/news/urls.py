from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', PostsList.as_view(), name='news'),
    path('search/', PostsSearchList.as_view(), name='post_search'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('account/<int:pk>/', PersonalAccountView.as_view(), name='personal_account'),
]
