from django.urls import path
from .views import PostsList, PostDetail, PostsSearchList, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostsList.as_view()),
    path('search/', PostsSearchList.as_view(), name='post_search'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

]
