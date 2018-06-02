from django.contrib import admin
from shareShack.models import Organization, Borrower, Item

# Register your models here.
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]

admin.site.register(Organization, OrganizationAdmin)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'cardnumber',)
    search_fields = ['last_name', 'cardnumber',]

admin.site.register(Borrower, BorrowerAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','writtenId', 'department', 'due_Back')
    search_fields = ['name','writtenId', 'department', ]

admin.site.register(Item, ItemAdmin)

'''
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('id','dateIssued','borrower',)
    search_fields = ['borrower','items']

admin.site.register(CheckOut, CheckoutAdmin)

class ReturnAdmin(admin.ModelAdmin):
    list_display = ('id','dateReturned','borrower',)
    search_fields = ['borrower','items']

admin.site.register(Return, ReturnAdmin)
'''
