# coding: utf-8
import re
from django import forms
from django.forms import Textarea, HiddenInput
from django.http import Http404
from django.shortcuts import get_object_or_404

from comments.models import PostComment


class PostCommentForm(forms.ModelForm):
    parent = forms.IntegerField(required=False, widget=HiddenInput)
    text = forms.CharField(
        max_length=700,
        widget=Textarea(attrs={'class': 'form-control', 'placeholder': u'Ваш комментарий...',
                               'rows': 6})
    )

    class Meta:
        model = PostComment
        fields = 'parent', 'text'

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not re.sub(r'\s+', '', text):
            raise forms.ValidationError(u'Комментарий не может состоять из одних пробелов.')
        return text
