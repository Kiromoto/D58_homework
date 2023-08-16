from datetime import datetime, timezone
from .models import Subscriber, Post
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def weekly_mails():
    print(
        f'Print from TASKS.py! weekly_mails {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}')
    users_emails = []
    start_time = datetime.now(tz=timezone.utc)
    try:
        for user_one in User.objects.all():
            user_subscription = Subscriber.objects.filter(user=user_one).values_list("category", flat=True)
            if user_one.email and user_subscription:
                last_news = Post.objects.filter(category__in=user_subscription, is_new=True).distinct()
                if last_news:
                    subject = f'Привет, {user_one.username}! Мы собрали для тебя подборку последних новостей!!!'
                    html_content = render_to_string('email_weekly.html',
                                                    {'last_news': last_news}
                                                    )
                    msg = EmailMultiAlternatives(subject=subject,
                                                 from_email=settings.EMAIL_HOST_USER,
                                                 to=[user_one.email],
                                                 )
                    msg.attach_alternative(html_content, 'text/html')
                    msg.send()

    except Exception:
        print('Ошибка получения данных о категории!')
    else:
        Post.objects.filter(datetime__lte=start_time, is_new=True).update(is_new=False)






