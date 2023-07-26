from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'datetime': ['lt', 'gt'],
            'category': ['exact'],
            'title': ['icontains'],
            'text': ['icontains'],
            'rating': ['lt', 'gt'],
            # 'isnew': ['true', 'false'],
        }
