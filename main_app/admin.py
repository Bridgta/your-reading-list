from django.contrib import admin
# import your models here
from .models import Reading, Read, Note

# Register your models here
admin.site.register(Reading)
admin.site.register(Read)
admin.site.register(Note)