from django.urls import path
from .views import PostList, PostDetail, PostUpdate, add_new, PostDelete, send_mail_example, become_an_author
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', PostList.as_view(), name='all_news'),
    path('<int:pk>', PostDetail.as_view(), name='new_detail'),
    path('add/', add_new, name='add_new'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='update_new'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='delete_new'),
    path('sendemail/', send_mail_example, name='send_mail_example'),
    path('becomeanauthor/', become_an_author, name='become_an_author'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
