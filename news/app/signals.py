from django.db.models.signals import post_save, m2m_changed
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Post, PostCategory, Category, Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, action, **kwargs):
    print(f"instance {instance}")
    emails = []
    try:
        instance_category = PostCategory.objects.filter(post_id=instance.id).values_list('category_id', flat=True)
        print(f'Try instance_category {instance_category}')

        users_emails = User.objects.filter(pk__in=Subscriber.objects.filter(category__in=instance_category).values_list('user', flat=True)).values_list('email', flat=True)
        print(f"User.objects.filter(pk__in=m) === {users_emails}")

        instance_category_name = PostCategory.objects.filter(post_id=instance.id).values_list('category_id__name', flat=True)
        print(f'Try instance_category_name {" ".join(list(instance_category_name))}')
    except Exception:
        print('Ошибка получения данных о категории')
    else:
        subject = f'Новая публикация в вашей любимой категории {" ".join(list(instance_category_name))}'
        html_content = render_to_string('email_new_add.html',
                                        {
                                            'post': instance,
                                            'url': f'http://127.0.0.1:8000{instance.get_absolute_url()}',
                                        }
                                        )

        for email in list(users_emails):
            msg = EmailMultiAlternatives(subject=subject,
                                         body=instance.text[:20],
                                         from_email=settings.EMAIL_HOST_USER,
                                         to=[email],
                                         )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    finally:
        print(f'Print emails from signals.py: {emails}')
