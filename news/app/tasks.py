from datetime import date, timedelta
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def weekly_mails():
    print(f'Print from TASKS.py every 5 seconds! weekly_mails {datetime.datetime}')
    # try:
    #     for user_one in User.objects.all():
    #         user_cat = []
    #         user_cat.clear()
    #         user_posts = []
    #         user_posts.clear()
    #         cat = CategorySubscriber.objects.filter(subscriber_user_id=user_one.id).values('category_name')
    #         print(f'User: {user_one.username}. Его e-mail: {user_one.email}. И подписан он на категории {cat}')
    #         if cat and user_one.email:
    #             for el in cat:
    #                 user_cat.append(el["category_name"])
    #
    #             for cat_id in user_cat:
    #                 cat_p = PostCategory.objects.filter(category_id=cat_id).values('post_id')
    #                 for i in cat_p:
    #                     if Post.objects.get(id=i['post_id']) not in user_posts:
    #                         d = Post.objects.get(id=i['post_id']).post_create_datetime
    #                         if d.date() >= (date.today() - timedelta(days=7)):
    #                             user_posts.append(Post.objects.get(id=i['post_id']))
    #
    #         if user_posts:
    #             print(
    #                 f'У юзера {user_one.username}, e-mail: {user_one.email} насобирались новости на отправку: {user_posts}')
    #             subject = _('Здравствуйте,') + user_one.username + '.' + _(
    #                 'Here are the most interesting news from the past week on NewsPaper')  # вот самые интересные новости за прошлую неделю на NewsPaper
    #             ur = []
    #             ur.clear()
    #             for p in user_posts:
    #                 ur.append({p: f'http://127.0.0.1:8000{p.get_absolute_url()}'})
    #
    #             html_content = render_to_string('send_everyweek.html', {'ur': ur, })
    #             msg = EmailMultiAlternatives(subject=subject, from_email='tlfordjango@mail.ru', to=[user_one.email, ], )
    #             msg.attach_alternative(html_content, 'text/html')
    #
    #             try:
    #                 msg.send()
    #             except Exception as e:
    #                 print(f'Не удалось отправить письмо на почтовый адрес: {user_one.email}. Ошибка: {e}')
    #
    # except Exception as e:
    #     print(f'Ошибка получения данных из db. {e}')
