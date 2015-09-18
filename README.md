# django-natural-time
A simple Django template tag to format times.

## Usage
Simply add the code in `natural_time.py` into one of your template tag files. For more information on how to write custom template tags, see https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/.

The `natural_time` tag formats times similar to the way Facebook does. Although there's a built-in `naturaltime` template tag in `django.contrib.humanize`, I wasn't satisfied with the way it *never* reverted back to displaying full dates, instead displaying something ugly like "203 days ago." So, I wrote this minor modification.

You use it like you would any other Django filter. For example:

```
{% load natural_time %}
...
Published {{ pub_date|natural_time }}
# Output might be:
# Published now
# Published 3 seconds ago
# Published 4 hours ago
# Published yesterday at 2:32 pm
# Published September 9, 2015 at 2:32 pm
```
