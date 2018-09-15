from django.db import models


class CreatedAtMixin(models.Model):
    created_at = models.DateTimeField(u'дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(u'дата последнего изменения', auto_now=True)

    class Meta:
        abstract = True
