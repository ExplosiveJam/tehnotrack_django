# coding: utf-8
from django import forms
from blogs.models import Post, Blog


class PostListForm(forms.Form):
    choices = (
        ('-created_at', u'сначала новые'),
        ('created_at', u'сначала старые'),
    )
    order_by = forms.ChoiceField(choices=choices, initial=choices[0], required=False, label=u'Упорядочить по дате')
    search = forms.CharField(required=False, label=u'Поиск по названию')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'title', 'text', 'blog'


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = 'title', 'description'