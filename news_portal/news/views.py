from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
from .forms import PostForm
from .models import Post, User, Category


# Create your views here.
class PostsList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'news/posts.html'
    context_object_name = 'news'
    paginate_by = 10
    permission_required = (
        'news.view_post',
    )


class PostsSearchList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'news/search.html'
    context_object_name = 'news'
    paginate_by = 10
    permission_required = (
        'news.view_post',
    )

    def get_queryset(self):
        self.queryset = PostFilter(self.request.GET, queryset=super().get_queryset())
        return self.queryset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.queryset
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'news'


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'news/post_create.html'
    form_class = PostForm
    permission_required = (
        'news.view_post',
        'news.add_post',
    )


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news/post_edit.html'
    form_class = PostForm
    permission_required = (
        'news.view_post',
        'news.change_post',
    )

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = (
        'news.view_post',
        'news.delete_post',
    )


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'flatpages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class PersonalAccountView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/personal_account.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['pk']  # Получаем значение идентификатора пользователя из URL
        context['user'] = User.objects.get(id=user_id)  # Получаем конкретного пользователя по его ID
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscriber.add(user)
    return render(request, 'news/subscribe.html', {'category': category})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscriber.remove(user)
    return render(request, 'news/unsubscribe.html', {'category': category})
