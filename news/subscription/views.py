from django.shortcuts import render
from app.models import Subscriber, Category
from django.db.models import Exists, OuterRef
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST.get('category_id'))
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscriber.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscriber.objects.filter(
                user=request.user,
                category=category,
            ).delete()

    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(Subscriber.objects.filter(user=request.user, category=OuterRef('pk'), ))
    ).order_by('name')

    return render(
        request,
        'subscriptions.html',
        {'categories': categories_with_subscriptions},
    )
