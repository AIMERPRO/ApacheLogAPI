from django.contrib import admin

from apacheAPI.models import Log


class LogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Log, LogAdmin)