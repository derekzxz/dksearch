from django.contrib import admin
from .models import Leader


class LeaderAdmin(admin.ModelAdmin):
    list_display = ['person', 'title', 'company', 'industry', 'geography']


admin.site.register(Leader, LeaderAdmin)
