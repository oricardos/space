from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_posted')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('is_posted',)
    list_per_page = 10

admin.site.register(Article, ArticleAdmin)
