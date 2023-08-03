from django import forms
from .models import Post, Author, Category
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    # category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), widget=forms.Select, required=False, )
    title = forms.CharField(label='Заголовок', required=True, )
    text = forms.CharField(required=True, widget=forms.Textarea, label='Текст статьи')
    picture = forms.FileField(label='Загрузите картинку для статьи', required=False, )

    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'text',
            'picture',
        ]

