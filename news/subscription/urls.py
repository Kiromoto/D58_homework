from django.urls import path
from .views import SubscribersNews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', SubscribersNews.as_view(), name='all_subscription'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
