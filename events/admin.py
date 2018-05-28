from django.contrib import admin
from events.models import Potluck, Host

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ['title',]


admin.site.register(Potluck, EventAdmin)

class HostAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]


admin.site.register(Host, HostAdmin)
