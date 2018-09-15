# coding: utf-8
from django.db import models
from django.conf import settings

from core.helper_models import CreatedAtMixin
from likes.models import LikeMixin


class Blog(CreatedAtMixin):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'автор', related_name='blogs')
    title = models.CharField(max_length=255, default='', verbose_name=u'название блога')
    description = models.CharField(max_length=500, default='', verbose_name=u'описание')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Блог'
        verbose_name_plural = u'Блоги'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return ' '.join((self.title, 'by', str(self.author)))

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogs:blog_detail', args=[str(self.id)])


class Category(CreatedAtMixin):
    name = models.CharField(max_length=255, default='', verbose_name=u'название категории', unique=True)
    description = models.CharField(max_length=1000, default='', verbose_name=u'описание категории')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('categories:category_detail', args=[str(self.id)])


class Post(CreatedAtMixin, LikeMixin):
    title = models.CharField(u'Название поста', max_length=255)
    text = models.TextField(max_length=10000, default='')
    categories = models.ManyToManyField('Category', related_name='posts', verbose_name=u'категории')
    blog = models.ForeignKey('Blog', related_name='posts', verbose_name=u'блог')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('posts:post_detail', args=[str(self.id)])

    @property
    def comments(self):

        def flatten(lst):
            res = []
            for el in lst:
                flatten(el) if isinstance(el, list) else res.append(el)
            return res

        comment_set = self.comment_set.all()
        if len(comment_set) == 0:
            return comment_set.all()
        comments = comment_set.filter(level=0).order_by('created_at')
        comment_set = comment_set.difference(comments)
        comments = list(comments)
        for i in range(0, 9):
            parents = comment_set.filter(level=i)
            for parent in parents:
                children = parent.answers.order_by('created_at')
                comment_set = comment_set.difference(children)
                children = list(children)
                comments.insert(comments.index(parent) + 1, children)
            flatten(comments)
        return comments
