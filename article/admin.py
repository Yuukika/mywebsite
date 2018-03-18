from django.contrib import admin
from .models import ArticlePost, Tag, Category

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ["title",]
admin.site.register(ArticlePost, ArticlePostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
