from django.contrib import admin

from .models import Post, Category

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [PostInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
