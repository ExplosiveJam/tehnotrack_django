# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PostComment


@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = 'id', 'post', 'text', 'author'
    list_editable = 'text',
