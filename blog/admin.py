from django.contrib import admin
from blog.models import Topic, Entry, Author, Tag, Comment, Image

# Register your models here.
class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class TopicAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Topic._meta.fields]
    inlines = [ImageInline]

    class Meta:
        model = Topic


admin.site.register(Topic, TopicAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entry._meta.fields]

    class Meta:
        model = Entry


admin.site.register(Entry, EntryAdmin)
admin.site.register(Author)


class TagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tag._meta.fields]
    inlines = [TopicInline]

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)


class ImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Image._meta.fields]

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)