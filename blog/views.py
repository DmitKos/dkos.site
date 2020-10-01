from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, Tag, Comment, Image
from .forms import CommentForm

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     """Домашняя страница приложения blog"""
#     return render(request, 'blog/index.html')


def index(request):
    """Выводим список тем (Topic)
    по убыванию, от новых к старым"""
    topics = Topic.objects.all
    entry = Entry.objects.order_by('-date')
    image = Image.objects.all
    paginator = Paginator(entry, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'topics': topics, 'entry': entry, 'image': image, 'page_obj': page_obj}
    return render(request, 'blog/index.html', context)


def topics(request):
    """Выводим список тем (Topic)"""
    topics = Topic.objects.order_by('title')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)


def topic(request, slug):
    """Вьюшка для каждой отдельной страницы (Topic)"""
    topic = get_object_or_404(Topic, slug__iexact=slug)
    entry = topic.entry_set.all
    image = topic.image_set.order_by('id')
    context = {'topic': topic, 'entry': entry, 'image': image}
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


def comments(request):
    """Представление для страницы со всеми комментариями"""
    comments = Comment.objects.order_by('-date')
    context = {'comments': comments}
    return render(request, 'blog/comments.html', context)


def comments_entry(request, slug):
    """Комментарии принадлежащие определённой записи (Entry)"""
    e_comment = get_object_or_404(Entry, slug__iexact=slug)
    comments = e_comment.comment_set.order_by('-date')
    e_text = e_comment.text
    e_topic = e_comment.topic
    context = {'comments': comments, 'e_text': e_text, 'e_topic': e_topic, 'e_comment': e_comment}
    return render(request, 'blog/comments_entry.html', context)


def new_comment(request, slug):
    """Представление для страницы для добавления нового комментария"""
    entry = get_object_or_404(Entry, slug__iexact=slug)
    topic = entry.topic
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.comment_entry_id = entry.id
            new_comment.slug = slug
            new_comment.save()
            return HttpResponseRedirect(reverse('blog:comments_entry', args=[entry.slug]))
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'blog/new_comment.html', context)


def site_search(request):
    topics = Topic.objects.order_by('-date')
    entries = Entry.objects.order_by('-date')
    search_query = request.GET.get('search', '')
    if search_query:
        topics = Topic.objects.filter(Q(title__icontains=search_query))
        entries = Entry.objects.filter(Q(text__icontains=search_query))
    context = {'topics': topics, 'entries': entries}
    return render(request, 'blog/search.html', context)