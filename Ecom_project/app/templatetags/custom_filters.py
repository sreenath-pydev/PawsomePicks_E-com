from django import template
import re

register = template.Library()
@register.filter(name='remove_numbers')
def remove_numbers(value):
    """Remove numbers from the username."""
    if isinstance(value, str):
        return re.sub(r'\d', '', value)  # Remove digits
    return value
