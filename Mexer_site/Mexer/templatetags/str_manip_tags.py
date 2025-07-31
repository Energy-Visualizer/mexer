from django import template
import re

register = template.Library()

@register.filter
def split(value, token):
    """Splits a given string into substrings bounded between some regex token"""
    return re.split(token, value)
