from django import forms
from .models import Post, Author, Category
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(), required=True, )
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

    def clean_new_added(self):
        new_added = self.cleaned_data["title"]
        print(f'title = cleaned_data.get === {new_added}')
        if new_added is not None and len(new_added) < 10:
            raise ValidationError("Заголовок статьи не может быть менее 10 символов.")

        return new_added
