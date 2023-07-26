from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateFilter, DateFromToRangeFilter,BooleanFilter
from django_filters.widgets import SuffixedMultiWidget, BooleanWidget
from django.forms import DateInput
from .models import Post, Author, Category


class RangeWidget(SuffixedMultiWidget):
    suffixes = ['min', 'max']


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(queryset=Category.objects.all(),
                                         lookup_expr='in',
                                         label='Категории',
                                         empty_label='Все категории',
                                         )
    author = ModelChoiceFilter(queryset=Author.objects.all(),
                               lookup_expr='exact',
                               label='Автор',
                               empty_label='Все авторы',
                               )
    # datetime = DateFilter(field_name='dt_create',
    #                       lookup_expr='gt', label='Опубликовано после',
    #                       widget=DateInput(attrs={'type': 'date'}),
    #                       )
    # datetime.field.error_messages = {'invalid': 'Введите дату в формате DD.MM.YYYY. Например: 23.10.2022'}
    # datetime.field.widget.attrs = {'placeholder': 'DD.MM.YYYY'}

    datetime = DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}),)
    is_new = BooleanFilter(widget=BooleanWidget(),)

    class Meta:
        model = Post
        fields = ['category', 'author', 'datetime', 'is_new']
        # fields = {
        #     'author': ['exact'],
        #     'datetime': ['lt'],
        #     'category': ['category__name'],
        #     'title': ['icontains'],
        #     'text': ['icontains'],
        #     'rating': ['lt', 'gt'],
        #     # 'isnew': ['true', 'false'],
        # }
