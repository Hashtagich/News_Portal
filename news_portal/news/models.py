from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    rating_user = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        """Метод, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
        Он состоит из следующего:
        суммарный рейтинг каждой статьи автора умножается на 3;
        суммарный рейтинг всех комментариев автора;
        суммарный рейтинг всех комментариев к статьям автора."""
        res1 = 0  # суммарный рейтинг каждой статьи автора умножается на 3;
        res2 = 0  # суммарный рейтинг всех комментариев автора;
        res3 = 0  # суммарный рейтинг всех комментариев к статьям автора.
        self.rating_user += sum((res1, res2, res3))
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    POSITIONS = [
        ('sport', 'спорт'),
        ('politics', 'политика'),
        ('education', 'образование ')
    ]

    choose_news = models.CharField(max_length=255, choices=POSITIONS)
    datetime_post = models.DateTimeField(auto_now_add=True)
    title_news = models.CharField(max_length=255, default='Заголовок статьи/новости')
    text_news = models.TextField(ddefault='Текст статьи/новости')
    rating_news = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Author
    products = models.ManyToManyField(Category, through='PostCategory',
                                      on_delete=models.CASCADE)  # связь «многие ко многим» с моделью Category

    def like(self):
        """Метод увеличивает рейтинг на единицу."""
        self.rating_news += 1
        self.save()

    def dislike(self):
        """Метод уменьшает рейтинг на единицу."""
        self.rating_news -= 1
        self.save()

    def preview(self):
        """Метод возвращает начало статьи (пред-ый просмотр) длиной 124 символа и добавляет многоточие в конце"""
        preview_length = 124
        if len(self.text_news) <= preview_length:
            return self.text_news
        else:
            return self.text_news[:preview_length] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Category


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # связь «один ко многим» с моделью Post
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # связь «один ко многим» со встроенной моделью User
    text_comment = models.TextField(ddefault='Комментарий')
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        """Метод увеличивает рейтинг на единицу."""
        self.rating_comment += 1
        self.save()

    def dislike(self):
        """Метод уменьшает рейтинг на единицу."""
        self.rating_comment -= 1
        self.save()
