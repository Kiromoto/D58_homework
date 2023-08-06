import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    avatar = models.FileField(upload_to='uploads/', blank=True, verbose_name='Загрузить аватарку', default='uploads/ava_default.png')

    def update_rating(self):
        # # суммарный рейтинг каждой статьи автора умножается на 3;
        # # !!! если у автора нет постов, то выдает ошибку. Нужно проверить.
        # sum_post_rating = self.post_set.aggregate(allPostRating=models.Sum('rating'))
        # postR = 0
        # postR += sum_post_rating.get('allPostRating')

        # суммарный рейтинг всех комментариев автора;
        # sum_comment_rating = self.author_user.comment_set.aggregate(authorCommentRating=models.Sum('comment_rating'))
        # commR = 0
        # commR += sum_comment_rating.get('authorCommentRating')

        # # # # суммарный рейтинг всех комментариев к статьям автора.
        # # sum_PostComment_rating = self.author_user.post.postComment_set.aggregate(allCommentPostRating=models.Sum('comment_rating'))
        # # pcommR = 0
        # # pcommR += sum_PostComment_rating.get('allCommentPostRating')
        #
        # self.author_rating = postR * 3 + commR  # + pcommR
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, help_text='category name')
    subscriber_c = models.ManyToManyField(User, through='Subscriber', blank=True)

    def get_subscribers(self):
        return ';\n'.join([s.username for s in self.subscriber_c.all()])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(f'HttpResponseRedirect(settings.LOGIN_REDIRECT_URL) === {HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)}')
        print(f'settings.ALLOWD_HOST+settings.LOGIN_REDIRECT_URL === {settings.ALLOWD_HOST+settings.LOGIN_REDIRECT_URL}')
        # return reverse('all_news', kwargs={'category': self.id})
        return settings.ALLOWD_HOST+settings.LOGIN_REDIRECT_URL


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory', related_name='posts')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    is_new = models.BooleanField(default=True)
    picture = models.FileField(upload_to='uploads/', blank=True, verbose_name='Загрузить картинку для новости', default='uploads/default.jpg')

    def get_category(self):
        return '\n'.join([c.name for c in self.category.all()])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.user}: {self.text}. Datetime: {datetime.date}. Rating: {self.rating}'
