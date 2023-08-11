from django.shortcuts import render
from app.models import Subscriber, Category
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


class SubscribersNews(ListView):
    model = Category
    ordering = 'name'
    template_name = 'subscriptions.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subscribtions'] = Subscriber.objects.all()

        context['subscribtions'] = Subscriber.objects.filter(user=self.request.user).values('category')
        print(f'user=self.request.user === {self.request.user}')
        print(f' context["subscribtions"] === {list(context["subscribtions"])}')
        print(f' context["category"] === {list(context["category"])}')

        # context['new_categories'] = list(PostCategory.objects.filter(post_id_id=context['single_post'].id))
        # context['last_news'] = list(Post.objects.order_by('-datetime')[:7])
        # context['new_comments'] = list(Comment.objects.order_by('-datetime').filter(post=context['single_post']))
        # self.object = self.get_object()
        # context['post_author_user'] = self.object.author.user

        return context


    # def get_filter(self):
    #     return PostFilter(self.request.GET, queryset=super().get_queryset())
    #
    # def get_queryset(self):
    #     return self.get_filter().qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.get_filter()
    #     return context

