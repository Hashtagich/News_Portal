from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'datetime_post': ['lt'],
            'title': ['icontains'],
            'author': ['exact'],
        }
