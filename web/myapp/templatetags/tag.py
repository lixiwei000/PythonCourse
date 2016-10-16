from django import template
from django.template.base import *

register = template.Library()


@register.simple_tag
def mySimpleTag(id):
    return int(id) * 1000
