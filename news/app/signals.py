from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Post
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@receiver(post_save, sender=Post)
def post_created(instance, created, **kwargs):
    if not created:
        return

    # emails = User.objects.filter(subscribers__category=instance.category).values_list('email', flat=True)
    # subject = f'Новая публикация в вашей любимой категории {instance.category}'
    #
    # html_content = render_to_string('email_new_add.html',
    #                                 {
    #                                     'post': instance,
    #                                     'url': f'http://127.0.0.1:8000{instance.get_absolute_url()}',
    #                                 }
    #                                 )
    #
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject=subject,
    #                                  body=instance.post_text[:20],
    #                                  from_email=settings.EMAIL_HOST_USER,
    #                                  to=email,
    #                                  )
    #     msg.attach_alternative(html_content, 'text/html')
    #     msg.send()
