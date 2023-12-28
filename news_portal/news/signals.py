from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from news_portal.settings import SITE_URL, EMAIL_HOST_USER
from .models import PostCategory


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


@receiver(m2m_changed, sender=PostCategory)
def notify_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subs = []
        for i in categories:
            subs += i.subscriber.all()

        subs_mail = [sub.email for sub in subs]

        send_notifications(
            preview=instance.preview(),
            pk=instance.pk,
            title=instance.title,
            sub_list=subs_mail,
        )
