# coding: utf-8
from django.contrib.auth.models import AbstractUser
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from blogs.models import Post


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars', blank=True, null=True)
    avatar_thumbnail = ImageSpecField(
        source='avatar',
        processors=[ResizeToFit(width=50, height=50)],
        format='JPEG',
        options={'quality': 90})
    about = models.CharField(u'о себе', max_length=1000, blank=True)
    birthday = models.DateField(u'дата рождения', null=True, blank=True)

    def __str__(self):
        return self.get_username()

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:profile', args=[str(self.id)])

    @property
    def posts(self):
        blogs = self.blogs.all()
        if not blogs:
            return None
        from django.db.models import Q
        posts = Post.objects.all()
        q = Q()
        for blog in blogs:
            q = q | Q(blog=blog)
        return posts.filter(q)
