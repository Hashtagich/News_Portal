from django.forms import DateInput
from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post


class PostFilter(FilterSet):
    datetime_post = DateFilter(
        field_name='datetime_post',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='date__gte',
        label='Дата'
    )
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название заголовка'
    )
    author = CharFilter(
        field_name='author__user__username',
        lookup_expr='icontains',
        label='Автор')

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'datetime_post'
        ]
