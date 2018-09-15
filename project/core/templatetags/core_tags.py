from django import template

register = template.Library()


@register.inclusion_tag('core/pretty_user.html')
def prettyuser(user, width="24px"):
    return {'user': user, 'width': width}
