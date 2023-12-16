from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category', 'choose_news', 'author']
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'category': 'Категория',
            'choose_news': 'Тип',
            'author': 'Автор'
        }
