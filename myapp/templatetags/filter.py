from django import template
register = template.Library()

@register.filter(name='myfilter')
def myfilter(value):
    return str(value).split('/')[-1]
