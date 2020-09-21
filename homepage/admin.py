from django.contrib import admin

from homepage.models import Hierarchy

from mptt.admin import DraggableMPTTAdmin

# Register your models here.

admin.site.register(Hierarchy, DraggableMPTTAdmin)
