# coding: utf-8
from comments.forms import PostCommentForm
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog, Post, Category
from django.shortcuts import reverse, get_object_or_404


class BlogList(ListView):
    model = Blog
    template_name = "blogs/bloglist.html"
    context_object_name = 'blog_list'
    paginate_by = 20


class PostList(ListView):
    model = Post
    template_name = "blogs/postlist.html"
    context_object_name = 'post_list'
    paginate_by = 20

    def get_queryset(self):
        q = super(PostList, self).get_queryset()
        self.form = PostListForm(self.request.GET)
        if self.form.is_valid():
            cd = self.form.cleaned_data
            if cd['order_by']:
                q = q.order_by(cd['order_by'])
            if cd['search']:
                q = q.filter(title__icontains=cd['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['searchform'] = self.form
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "blogs/post.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        if self.request.user.is_authenticated:
            commentform = PostCommentForm()
            context['commentform'] = commentform
        return context


class BlogDetail(ListView):
    model = Post
    template_name = "blogs/blog.html"
    paginate_by = 10
    context_object_name = 'post_list'

    def dispatch(self, request, *args, **kwargs):
        self.blog = get_object_or_404(Blog, pk=kwargs['pk'])
        return super(BlogDetail, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = super(BlogDetail, self).get_queryset()
        q = q.filter(blog=self.blog)
        return q

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data()
        context['blog'] = self.blog
        return context


class CategoryList(ListView):
    model = Category
    template_name = "blogs/categorylist.html"
    context_object_name = 'category_list'
    paginate_by = 20


class CategoryDetail(ListView):
    model = Post
    template_name = "blogs/category.html"
    paginate_by = 20
    context_object_name = 'post_list'

    def dispatch(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, pk=kwargs['pk'])
        return super(CategoryDetail, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = super(CategoryDetail, self).get_queryset()
        q = q.filter(categories__in=[self.category])
        return q

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data()
        context['category'] = self.category
        return context



#Create and Update views

class BlogCreate(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = "blogs/blogcreate.html"

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreate, self).form_valid(form)


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = 'title', 'description'
    template_name = "blogs/blogupdate.html"

    def get_queryset(self):
        return super(BlogUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blogs:blog_detail', kwargs={'pk': self.object.pk})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = 'title', 'text', 'categories', 'blog'
    template_name = "blogs/postcreate.html"

    def dispatch(self, request, pk=None, *args, **kwargs):
        if pk:
            self.blog = get_object_or_404(Blog.objects.all(), id=pk)
        return super(PostCreate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    template_name = "blogs/postupdate.html"
