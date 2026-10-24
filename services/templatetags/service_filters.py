from django import template

register = template.Library()

@register.filter
def phone_display(phone):
    return f"{phone[:4]} {phone[4:7]} {phone[7:]}"