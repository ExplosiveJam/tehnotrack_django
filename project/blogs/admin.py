# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, Category, Blog
from comments.models import PostComment


class CommentInline(admin.TabularInline):
   model = PostComment


class PostInline(admin.TabularInline):
    model = Post


class CategoryInline(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at', 'blog'
    list_editable = 'title',
    list_per_page = 40
    inlines = CategoryInline, CommentInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'posts'
    list_editable = 'name',


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_editable = 'title',
    inlines = PostInline,
