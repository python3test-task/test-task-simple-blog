from django.contrib import admin
from .models import Post, Contact


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created')
    prepopulated_fields = {'slug': ('title',)}          # автоматически создаем slug из title


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_from', 'user_to', 'created',)

