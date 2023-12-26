from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news_portal.settings import EMAIL_HOST_USER


class BaseRegisterForm(UserCreationForm, SignupForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    def save(self, request):
        user = super(BaseRegisterForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)

        # Отправка сообщения с помощью шаблона html при регистрации через
        # from django.core.mail import EmailMultiAlternatives
        # from django.template.loader import render_to_string
        html_content = render_to_string(
            'letters/email_confirmation_signup_message.html',
            {
                'words': user,
            }
        )

        msg = EmailMultiAlternatives(
            subject='Регистрация успешно пройдена!',
            from_email=EMAIL_HOST_USER,
            to=[user.email],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html
        msg.send()  # отсылаем

        # Отправка сообщения при регистрации через from django.core.mail import send_mail
        # send_mail(
        #     subject='Приветствуем у нас на сайте!',
        #     message=f"{user.last_name} {user.first_name}, Вы успешно прошли регистрацию, поздравляем!",
        #     from_email=EMAIL_HOST_USER,
        #     recipient_list=[user.email]
        # )
        return user

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)
