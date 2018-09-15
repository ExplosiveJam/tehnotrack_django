# coding utf-8
from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404
from likes.models import LikeMixin
from core.helper_models import CreatedAtMixin


# Create your models here.


class PostComment(CreatedAtMixin, LikeMixin):
    parent = models.ForeignKey('PostComment', null=True, related_name='answers')
    post = models.ForeignKey('blogs.Post', related_name='comment_set')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'автор', related_name='comments')
    text = models.CharField(u'текст', max_length=700, blank=False)
    is_deleted = models.BooleanField(default=False)
    level = models.PositiveSmallIntegerField()

    def set_parent(self, id=None):
        if id and id != self.pk:
            self.parent = get_object_or_404(PostComment, pk=id)
        else:
            return

    def save(self, *args, **kwargs):
        if not self.pk:
            self.level = 0 if not self.parent else self.parent.level + 1
        super(PostComment, self).save(*args, **kwargs)
