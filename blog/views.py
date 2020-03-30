from django.shortcuts import render, get_object_or_404

from .models import Topic, Entry

# Create your views here.
def index(request):
    """Домашняя страница приложения blog"""
    return render(request, 'blog/index.html')


def topics(request):
    """Выводим список тем (Topic)
    по убыванию, от новых к старым"""
    topics = Topic.objects.order_by('-date')
    entry = Entry.objects.order_by('text')
    context = {'topics': topics, 'entry': entry}
    return render(request, 'blog/topics.html', context)


def topic(request, slug):
    topic = get_object_or_404(Topic, slug__iexact=slug)
    entry = topic.entry_set.all
    context = {'topic': topic, 'entry': entry}
    return render(request, 'blog/topic.html', context)