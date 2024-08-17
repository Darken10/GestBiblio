from django import template

register=template.Library()

@register.tag
@register.inclusion_tag('test.html')
def test(value):
    return {
        'value':value
    }