from django.contrib import admin
from blog.models import Topic, Entry, Author, Tag, Comment

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment)