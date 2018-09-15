from django import template

register = template.Library()


@register.inclusion_tag('blogs/helpers/li_post.html', takes_context=True)
def li_post(context, post):
    return {'post': post,
            'user': context['request'].user}


@register.inclusion_tag('blogs/helpers/li_blog.html', takes_context=True)
def li_blog(context, blog):
    return {'blog': blog,
            'user': context['request'].user}


@register.inclusion_tag('blogs/helpers/li_category.html')
def li_category(category):
    return {'category': category}
