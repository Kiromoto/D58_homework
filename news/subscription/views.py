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
        context['subscribtions'] = Subscriber.objects.filter(user=self.request.user)

        print(f' context["subscribtions"] === {context["subscribtions"]}')
        print(f' context["category"] === {context["category"]}')

        category_sub = []
        category_unsub = []

        for c in context["category"]:
            for el in context['subscribtions']:
                print(f'c= {c}  el.category= {el.category} c==el.category {c == el.category} c in category_sub {c in category_sub} c in category_unsub {c in category_unsub}')
                print(f'category_sub>>> {category_sub}')
                print(f'category_unsub>>> {category_unsub}')
                if (c == el.category) and (c not in category_sub):
                    category_sub.append(c)
                    break

            category_unsub.append(c)


        context["category_sub"] = category_sub
        context["category_unsub"] = category_unsub

        print(f' context["category_sub"] === {context["category_sub"]}')
        print(f' context["category_unsub"] === {context["category_unsub"]}')
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
