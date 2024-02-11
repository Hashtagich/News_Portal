from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from news.views import CategoryViewset, PostsViewset, AuthorViewset

router = routers.DefaultRouter()
router.register(r'posts', PostsViewset)
router.register(r'category', CategoryViewset)
router.register(r'author', AuthorViewset, basename='author')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('news.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='flatpages/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('api/', include(router.urls)),
]
