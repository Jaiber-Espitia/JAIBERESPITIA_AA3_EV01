from django import template

register = template.Library()


@register.filter
def total_price(product):
    return product.quanity * product.price 