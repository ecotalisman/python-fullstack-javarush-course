from django.urls import re_path
from .views import blog_archive

# Use re_path to define a route using a regular expression
urlpatterns = [
    # Regular expression for the URL:
    # ^blog/ - the URL must start with 'blog/'
    # (?P<year>\d{4}) - a group named 'year' accepts exactly 4 digits
    # (?P<month>\d{1,2}) - a group named 'month' accepts 1 or 2 digits
    # (?P<day>\d{1,2}) - a group named 'day' accepts 1 or 2 digits
    # /$ - the URL must end with the '/' character
    re_path(r'^blog/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', blog_archive, name='blog'),
]