from django import template

register = template.Library()


@register.inclusion_tag("partials/field_label.html")
def field_label(label, tooltip, link_url=None, link_text=None):
    return {
        "label": label,
        "tooltip": tooltip,
        "link_url": link_url,
        "link_text": link_text,
    }
