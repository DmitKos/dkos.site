from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from time import time
from django.urls import reverse

# генерируем slug: первая часть slug из модели, плюс символ "_" и
# плюс вторая часть из модуля time, который отсчитывает время 
# с 01 января 1970 года, затем приводим вторую часть в строковое
# значение
def slug_gen(s):
    new_slug = slugify(s)
    return new_slug + '_' + str(int(time()))


# Create your models here.
class Topic(models.Model):
    """Название темы"""
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    tag = models.ForeignKey('Tag', on_delete=models.PROTECT, blank=True, null=True)
    tags = models.ManyToManyField('Tags', blank=True)
    description = models.CharField(max_length=160, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:topic', args=[self.slug])


class Entry(models.Model):
    """Текст темы"""
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images/preview/', blank=True, null=True)
    image_s = models.ImageField(upload_to='images/preview/', blank=True, null=True)
    image_alt = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:100] + "..."


class Author(models.Model):
    """Автор темы"""
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    email = models.EmailField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return '%s %s' % (self.username, self.email)


class Tag(models.Model):
    """Теги темы"""
    text = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Old tags'

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('blog:tag', args=[self.slug])


class Tags(models.Model):
    """Теги темы"""
    text = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('blog:topic_tag_url', kwargs={'slug': self.slug})


class Comment(models.Model):
    """Комментарии относящиеся к теме"""
    text = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    comment_entry = models.ForeignKey('Entry', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slug_gen(self.author)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.text


class Image(models.Model):
    """Изображения для Topic"""
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_s = models.ImageField(upload_to='images/', blank=True, null=True)
    image_m = models.ImageField(upload_to='images/', blank=True, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT, blank=True, null=True)
    image_alt = models.CharField(max_length=40, blank=True)