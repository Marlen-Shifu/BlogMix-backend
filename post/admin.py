from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'publish_date')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'content', 'publish_date')


admin.site.register(Post, PostAdmin)