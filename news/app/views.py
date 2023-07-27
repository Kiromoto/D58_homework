from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Comment
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-datetime'
    template_name = 'all_news.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.get_filter()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'single_new.html'
    context_object_name = 'single_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_categories'] = list(PostCategory.objects.filter(post_id_id=context['single_post'].id))
        context['last_news'] = list(Post.objects.order_by('-datetime')[:7])
        context['new_comments'] = list(Comment.objects.order_by('-datetime').filter(post=context['single_post']))
        return context
