from random import choice, randint, sample, normalvariate
import string
from django.contrib.auth import get_user_model
from blogs.models import *


alphabet = {'en':string.ascii_lowercase,
                    'ru':'абвгдежзийклмнопрстуфхцчшщъыьэюя',
                    'punct':'.?!',
                    'digits':string.digits,
                    'w':' '}

def _randword():
    alp = alphabet[choice(['en', 'ru'])]
    p = abs(int(normalvariate(7, 4)))
    length = p if p > 0 else choice([1, 2, 3])
    return ''.join([choice(alp) for _ in range(length)])


def _randline():
    numwords = abs(int(normalvariate(10, 5))) + 1
    result = _randword().capitalize()
    result += ' '.join([_randword() for _ in range(numwords - 1)])
    result += choice(alphabet['punct'])
    return result


def _randtext(n):
    numlines = randint(n // 2, n)
    result = ' '.join([_randline() for _ in range(numlines)])
    return result


def _usr():
    return get_user_model().objects.all()


def fill_users(n):
    usr = get_user_model()
    for i in range(n):
        user = usr(username='Username' + str(i))
        user.save()


def fill_blogs(n):
    users = _usr()
    for i in range(n):
        blog = Blog(author=users[i] if i < len(users) else choice(users))
        blog.title = 'Title' + str(i)
        blog.description = 'description' + str(i)
        blog.save()


def fill_categories(n):
    for i in range(n):
        category = Category(name='Category#' + str(i))
        category.description = _randtext(5)
        category.save()


def fill_posts(n):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    for i in range(n):
        post = Post(title='Post#' + str(i))
        post.blog = blogs[i] if i < len(blogs) else choice(blogs)
        cat_list = sample(list(categories), randint(1, len(categories) // 3))
        post.text = _randtext(50)
        post.save()
        post.categories.set(cat_list)


def fill(users=40, blogs=55, categories=30, posts=200):
    fill_users(users)
    fill_blogs(blogs)
    fill_categories(categories)
    fill_posts(posts)


def clear():
    for user in get_user_model().objects.all():
        if not user.is_superuser:
            user.delete()
    for blog in Blog.objects.all():
        blog.delete()
    for category in Category.objects.all():
        category.delete()
    for post in Post.objects.all():
        post.delete()
