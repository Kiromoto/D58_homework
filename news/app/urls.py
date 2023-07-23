from django.urls import path
from .views import PostList, PostDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
