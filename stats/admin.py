from django.contrib import admin

# Register your models here.
# We need to tell the admin that Question objects have an admin interface. To do this, open the stats/admin.py file, and edit it to look like this:
from .models import Question

admin.site.register(Question)