from django import template
from num2words import num2words

register = template.Library()

@register.filter
def num_to_words(value):
    try:
        return num2words(int(value), to='cardinal', lang='en_IN').title()
    except Exception:
        return value