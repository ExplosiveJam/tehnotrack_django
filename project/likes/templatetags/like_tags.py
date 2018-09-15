from django import template

register = template.Library()


@register.inclusion_tag('likes/like.html')
def like(value, active=True):
    return {'likes': value.likes,
            'active': active}
