from django import template
from blog.models import Tag, Post
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('blog/sidebar.html')
def show_sidebar():
    tags = Tag.objects.annotate(count_post=Count('post'))
    return {'tags': tags,}
