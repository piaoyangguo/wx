__author__ = 'Administrator'
from django import template

register = template.Library()


@register.simple_tag
def pagenumber(list, path, pageno, orderby):
    pagenumberlist = ""
    for i in list:
        if i == pageno:
            active = "active"
        else:
            active = "n-active"
        a = "<li class='%s'><a href='%s'>%s</a></li>" % (active, path + '/' + "?pageno=" + str(i) + "&orderby=" + orderby, str(i))
        pagenumberlist += a
    return pagenumberlist