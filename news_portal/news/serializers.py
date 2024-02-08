from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'url', ]
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'pk'}
        }



class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'choose_news', 'datetime_post', 'rating', 'category', 'title', 'text', 'url',]
        extra_kwargs = {
            'url': {'view_name': 'post-detail', 'lookup_field': 'pk'}
        }
