from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.models import Post, Category
from news_portal.settings import EMAIL_HOST_USER, SITE_URL


@shared_task
def weekly_notification():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(datetime_post__gte=last_week)
    cat = set(posts.values_list('category__name', flat=True))
    subs = set(Category.objects.filter(name__in=cat).values_list('subscriber__email', flat=True))

    html_context = render_to_string(
        'account/email/email_weekly_posts.html',
        {
            'head_link': f'{SITE_URL}',
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Последние посты за неделю',
        body='',
        from_email=EMAIL_HOST_USER,
        to=subs,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()


@shared_task
def send_notifications(preview, pk, title, sub_list):
    html_context = render_to_string(
        'account/email/email_post_add.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/news/{pk}',
            'title': title,
        }
    )

    msg = EmailMultiAlternatives(
        subject=f'Новый пост',
        body='',
        from_email=EMAIL_HOST_USER,
        to=sub_list,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send()
