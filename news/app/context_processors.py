from .models import Category

def navigate_context(request):
    test = 'Оставь здесь свой отклик'

    context = {
        'vartest': test,
        'current_user': request.user,
        'categories': Category.objects.all(),
    }

    return context
