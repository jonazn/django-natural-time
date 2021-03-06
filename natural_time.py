from django import template
from planner.views import get_ref_name
from django.utils.translation import pgettext, ugettext as _, ungettext
from django.utils.timezone import is_aware, utc, get_current_timezone
from django.template import defaultfilters
from datetime import date, datetime, timedelta

register = template.Library()

@register.filter
def natural_time(value):
    """
    Returns a 'natural' representation of the given time.
    Formats similar to Facebook.
    Based on django.contrib.humanize.naturaltime
    
    If given time occurred today, prints 'x seconds/minutes/hours ago'
    If given time occurred yesterday, prints 'yesterday at xx:xx'
    If given time occurred more than 1 day ago, prints full date
    """
    if not isinstance(value, date):  # datetime is a subclass of date
        return value

    current_timezone = get_current_timezone()
    now = datetime.now(current_timezone)
    yesterday = now - timedelta(days=1)
    value = value.astimezone(current_timezone) # localize timezone

    delta = now - value
    if value.date() == yesterday.date():
        return _('yesterday at %(time)s') % {'time': defaultfilters.time(value, 'TIME_FORMAT')}
    elif delta.days != 0:
        return defaultfilters.date(value, 'DATETIME_FORMAT')
    elif delta.seconds == 0:
        return _('now')
    elif delta.seconds < 60:
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'a second ago', '%(count)s seconds ago', delta.seconds
        ) % {'count': delta.seconds}
    elif delta.seconds // 60 < 60:
        count = delta.seconds // 60
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'a minute ago', '%(count)s minutes ago', count
        ) % {'count': count}
    else:
        count = delta.seconds // 60 // 60
        return ungettext(
            # Translators: please keep a non-breaking space (U+00A0)
            # between count and time unit.
            'an hour ago', '%(count)s hours ago', count
        ) % {'count': count}