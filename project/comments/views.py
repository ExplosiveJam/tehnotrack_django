# coding utf-8

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, resolve_url, redirect
from django.views.generic import CreateView, ListView
from comments.forms import PostCommentForm
from comments.models import PostComment
from blogs.models import Post


class PostCommentCreate(CreateView, LoginRequiredMixin):
    model = PostComment
    fields = 'text',

    def get_success_url(self):
        return resolve_url('posts:post_detail', pk=self.postobject.id)

    def dispatch(self, request, *args, **kwargs):
        self.postobject = get_object_or_404(Post, pk=kwargs.get('pk'))
        return super(PostCommentCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.instance
        instance.author = self.request.user
        instance.post = self.postobject
        instance.set_parent(int(self.request.POST.get('parent')))
        return super(PostCommentCreate, self).form_valid(form)

        # instance = form.save(commit=False)
        # instance.author = self.request.user
        # instance.post = self.postobject
        # instance.set_parent(form.cleaned_data.get('parent'))
        # instance.save()
        # return redirect(self.get_success_url())

