from django.contrib import admin

from articles.models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('id', 'slug', 'creation_date', 'status', 'like_counter')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
