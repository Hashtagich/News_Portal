from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', cache_page(60*1)(PostsList.as_view()), name='news'),
    path('search/', cache_page(60*1)(PostsSearchList.as_view()), name='post_search'),
    path('news/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('account/<int:pk>/', PersonalAccountView.as_view(), name='personal_account'),
    path('category/<int:pk>/subscribe', subscribe, name='category_subscribe'),
    path('category/<int:pk>/unsubscribe', unsubscribe, name='category_unsubscribe'),
]
