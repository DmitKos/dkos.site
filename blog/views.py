from django.shortcuts import render, get_object_or_404

from .models import Topic, Entry, Tag

# Create your views here.
def index(request):
    """Домашняя страница приложения blog"""
    return render(request, 'blog/index.html')


def topics(request):
    """Выводим список тем (Topic)
    по убыванию, от новых к старым"""
    topics = Topic.objects.order_by('-date')
    entry = Entry.objects.all
    context = {'topics': topics, 'entry': entry}
    return render(request, 'blog/topics.html', context)


def topic(request, slug):
    """Вьюшка для каждой отдельной страницы (Topic)"""
    topic = get_object_or_404(Topic, slug__iexact=slug)
    entry = topic.entry_set.all
    context = {'topic': topic, 'entry': entry}
    return render(request, 'blog/topic.html', context)


def tags(request):
    """Вьюшка для страницы со всеми тегами"""
    tags = Tag.objects.order_by('text')
    context = {'tags': tags}
    return render(request, 'blog/tags.html', context)


def tag(request, slug):
    """Отдельное представление для каждого тега, каждый тег, в свою очередь,
    связан с определёнными темами (Topic)"""
    tag = get_object_or_404(Tag, slug__iexact=slug)
    tag_topics = tag.topic_set.order_by('title')
    context = {'tag': tag, 'tag_topics': tag_topics}
    return render(request, 'blog/tag.html', context)
