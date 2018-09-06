from django.contrib import admin

from .models import Area, Address

class AreaAdmin(admin.ModelAdmin):
    """ Area Admin """
    list_display = ('city', 'country', 'region', 'verified')
    list_display_links = ('city',)

    search_fields = ('city', 'country', 'region')
    list_filter = ('verified',)

    readonly_fields = ['created_at', 'updated_at']
    list_editable = ('verified',)
    #autocomplete_fields = ['owner',]

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('city', 'country', 'region',)
        }),
        ('Flags', {
            'fields': ('verified',),
        }),
        ('Internals', {
            'fields': ('created_at', 'updated_at',),
        }),
    )
admin.site.register(Area, AreaAdmin)



class AddressAdmin(admin.ModelAdmin):
    """ Address Admin """
    list_display = ('__str__', 'user', 'created_at')
    #list_display_links = ('city',)

    search_fields = ('street', 'street_number', 'zipcode', 'city', 'country')
    #list_filter = ('verified',)

    readonly_fields = ['created_at', 'updated_at']
    #list_editable = ('active', 'sharetype',)
    autocomplete_fields = ['area', 'user',]

    save_on_top = True
    fieldsets = (
        ('Address', {
            'fields': ('street', 'street_number', 'supplement', )
        }),
        ('Area', {
            'fields': ('zipcode', 'area',),
        }),
        ('Internals', {
            'fields': ('user', 'created_at', 'updated_at',),
        }),
    )
admin.site.register(Address, AddressAdmin)
