from django.contrib.sitemaps import Sitemap
from blog.models import Topic, Tag

class TopicSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Topic.objects.all()

    def lastmod(self, obj):
        return obj.date


class TagSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Tag.objects.all()