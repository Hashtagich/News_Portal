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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author
        fields = ['id', 'url', 'user', 'rating',]
        extra_kwargs = {
            'url': {'view_name': 'author-detail', 'lookup_field': 'pk'}
        }
