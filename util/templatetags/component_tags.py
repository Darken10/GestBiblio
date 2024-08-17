from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def render_component(component_name, **kwargs):
    return render_to_string(f"components/{component_name}.html", kwargs)
