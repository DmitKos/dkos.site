"""Схема URL для blog"""
from django.urls import path, include
from . import views

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import TopicSitemap, TagSitemap

sitemaps = {
    'topics': TopicSitemap,
    'tag': TagSitemap,
}

app_name = 'blog'
urlpatterns = [
    # домашняя страница
    #path('', views.index, name='index'),
    # домашняя страница
    path('', views.index, name='index'),
    # страница блога со списком постов (Topic)
    #path('topics/', views.topics, name='topics'),
    # страница для каждого поста (Topic)
    path('topics/<str:slug>/', views.topic, name='topic'),
    # страница со списком тегов (Tag)
    path('tags/', views.tags, name='tags'),
    # страницы для каждого тега (Tag)
    path('tags/<str:slug>/', views.tag, name='tag'),
    # страница с комментариями (Comment)
    #path('comments/', views.comments, name='comments'),
    # страница для каждого по отдельности комментария
    path('comments/<str:slug>/', views.comments_entry, name='comments_entry'),
    # страница для добавления нового комментария
    path('new_comment/<str:slug>/', views.new_comment, name='new_comment'),
    # поиск на сайте
    path('search/', views.site_search, name='site_search'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('topic_tags_list/', views.topic_tags_list, name='topic_tags_list_url'),
    path('topic_tag/<str:slug>/', views.topic_tag, name='topic_tag_url'),
]