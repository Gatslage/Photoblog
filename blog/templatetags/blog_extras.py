from atexit import register
import datetime
from django import template
import django

register=template.Library()

@register.filter
def filType(mot):
    return type(mot).__name__

@register.simple_tag(takes_context=True)
def nameperso(context,created):
    if context['user']==created:
        return 'Vous'
    return created.username

@register.simple_tag(takes_context=True)
def get_posted_at_display(context,date_created):
    now=django.utils.timezone.now()
    dtime=now-date_created
    final="il y'a"
    print(dtime.days)
    if dtime.days >=1:
        final+=" {} jours".format(dtime.days)
    if divmod(dtime.seconds,3600)[0]>=1:
        final+= " {} heures {} minutes".format(divmod(dtime.seconds,3600)[0],divmod(divmod(dtime.seconds,3600)[1],60)[0])
    elif divmod(dtime.seconds,60)[0]>=1:
        final+=" {} minutes".format(divmod(dtime.seconds,60)[0])
    return (final,' maintenant')[final=="il y'a"]
        
    