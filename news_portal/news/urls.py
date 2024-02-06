from django.urls import path, include
from .views import *
from news.views import CategoryViewset, PostViewset, AuthorViewest
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categorys', CategoryViewset)
router.register(r'posts', PostViewset)
router.register(r'authors', AuthorViewest)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', PostsList.as_view(), name='news'),
    path('search/', PostsSearchList.as_view(), name='post_search'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('account/<int:pk>/', PersonalAccountView.as_view(), name='personal_account'),
    path('category/<int:pk>/subscribe', subscribe, name='category_subscribe'),
    path('category/<int:pk>/unsubscribe', unsubscribe, name='category_unsubscribe'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
