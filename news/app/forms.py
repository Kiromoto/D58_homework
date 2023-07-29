from django import forms
from .models import Post, Author, Category


class PostForm(forms.ModelForm):
    # author = forms.ModelChoiceField(label='Автор', queryset=Author.objects.all(), required=True, )
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), required=True, )
    title = forms.CharField(label='Заголовок', required=True, )
    text = forms.CharField(label='Текст статьи', required=True, )
    picture = forms.FileField(label='Загрузите картинку для статьи', required=False, )

    class Meta:
        model = Post
        fields = [
            # 'author',
            'category',
            'title',
            'text',
            'picture',
        ]

