from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView
from django.conf import settings
from .models import Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = '-datetime'
    template_name = 'all_news.html'
    context_object_name = 'posts'
    paginate_by = 6

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


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'add_new.html'
    context_object_name = 'single_post'


# @login_required(login_url=settings.LOGINURL)
def add_new(request):
    print(f'request.user.is_authenticated === {request.user.is_authenticated}')
    print(f'request.user.author === {request.user.author}')
    if request.user.is_authenticated and request.user.author:
        if request.method == 'GET':
            form = PostForm()
            print(f'if request.method == "GET":')
            return render(request, 'add_new.html', {'form': form})

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            print(f'form.is_valid(): {form.is_valid()}')
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user.author
                post.save()
                return redirect(post.get_absolute_url())
            else:
                form = PostForm()
    else:
        print(f'if HttpResponseRedirect("/news/")')
        return HttpResponseRedirect('/news/')
