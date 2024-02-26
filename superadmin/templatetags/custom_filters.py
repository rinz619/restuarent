from django import template
from superadmin.models import *

register = template.Library()

@register.simple_tag()
def fetchuser(value):
    user = Customers.objects.get(id=value)
    return user.name
