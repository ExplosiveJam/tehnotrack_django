# coding utf-8
from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.user.username)


class LikeMixin(models.Model):
    likes = GenericRelation(Like, content_type_field='content_type', object_id_field='object_id')

    class Meta:
        abstract=True
