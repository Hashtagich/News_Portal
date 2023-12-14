from django.views.generic import ListView, DetailView

from .filters import PostFilter
from .models import Post


# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'posts.html'
    context_object_name = 'news'
    paginate_by = 1  # число означает кол-во отображаемых объектов на странице


class PostsSearchList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 1  # число означает кол-во отображаемых объектов на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'
