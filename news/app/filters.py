from django_filters import FilterSet, ModelChoiceFilter, DateFilter, CharFilter, ChoiceFilter
from django.forms import DateInput
from .models import Post, Author, Category


class PostFilter(FilterSet):
    category = ModelChoiceFilter(queryset=Category.objects.all(),
                                 lookup_expr='exact',
                                 label='По категории',
                                 empty_label='Все категории',
                                 )

    author = ModelChoiceFilter(queryset=Author.objects.all(),
                               lookup_expr='exact',
                               label='По автору',
                               empty_label='Все авторы',
                               )
    datetime = DateFilter(field_name='datetime',
                          lookup_expr='gt', label='Опубликовано после',
                          widget=DateInput(attrs={'type': 'date'}),
                          )
    datetime.field.error_messages = {'invalid': 'Введите дату в формате DD.MM.YYYY. Например: 23.10.2022'}
    datetime.field.widget.attrs = {'placeholder': '01.01.2023'}

    text = CharFilter(field_name='text', lookup_expr='icontains', label='В тексте')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='По заголовку')

    class Meta:
        model = Post
        fields = ['category', 'author', 'datetime', 'text', 'title', ]


class PostFilter2(FilterSet):
    class Meta:
        model = Post
        fields = ['category', 'author', 'datetime', 'text', 'title', ]
