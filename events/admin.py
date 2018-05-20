from django.contrib import admin
from events.models import Potluck

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ['title',]


admin.site.register(Potluck, EventAdmin)
