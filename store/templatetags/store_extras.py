from django import template

register = template.Library()

@register.filter
def make_range(value):
    """
    Given an integer 'value',
    return the value converted into a range.
    """
    return range(value)
