from django import template

register = template.Library()


@register.inclusion_tag('comments/comment.html')
def show_comment(comment, read_only=False):
    ml = (str(2 * comment.level) + 'rem') if not read_only else '0'
    return {'comment': comment,
            'ml': ml,
            'read_only': read_only}


@register.inclusion_tag('comments/comment_button.html')
def comment_button(post):
    comment_count = post.comment_set.count()
    return {'comment_count': comment_count,
            'post': post}
