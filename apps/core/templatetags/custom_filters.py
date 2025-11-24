from django import template

register = template.Library()

@register.filter
def in_group_or_superuser(user, group_name):
    """
    Returns True if the user belongs to the given group or is a superuser.
    """
    return user.is_superuser or user.groups.filter(name=group_name).exists()
