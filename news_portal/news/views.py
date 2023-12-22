from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, TemplateView

from .filters import PostFilter
from .forms import PostForm
from .models import Post


# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'news/posts.html'
    context_object_name = 'news'
    paginate_by = 10


class PostsSearchList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'news/search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        self.queryset = PostFilter(self.request.GET, queryset=super().get_queryset())
        return self.queryset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.queryset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'news'


class PostCreateView(CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'news/post_edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/home.html'
