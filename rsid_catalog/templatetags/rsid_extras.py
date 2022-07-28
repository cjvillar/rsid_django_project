from django import template
#from django.template.defaulttags import register
from rsid_catalog.models import Rsids


register = template.Library()

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)