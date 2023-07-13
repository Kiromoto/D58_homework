from django.contrib import admin
from .models import Author, Category, Post, Subscriber, PostCategory, Comment


def nullfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)


nullfy_rating.short_description = 'Обнулить рейтинг'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_subscribers',)
    search_fields = ('id', 'name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'get_category', 'rating', 'datetime',)
    list_filter = ('author', 'title', 'rating', 'datetime',)
    search_fields = ('title', 'text',)
    actions = [nullfy_rating]


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user', 'category',)
    search_fields = ('user', 'category',)
    search_filter = ('user', 'category',)


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'category_id',)
    list_filter = ('category_id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'rating', 'datetime',)
    search_fields = ('post', 'text',)
    actions = [nullfy_rating]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
