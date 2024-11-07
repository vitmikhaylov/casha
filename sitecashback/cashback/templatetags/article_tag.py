from django import template

from cashback.models import Category, Tag


register = template.Library()

@register.inclusion_tag('cashback/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.inclusion_tag('cashback/list_tags.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
