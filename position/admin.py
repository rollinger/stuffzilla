from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Area, Address, Language

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
    #list_editable = (s = ['area', 'user',]

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



class LanguageAdmin(TranslationAdmin):
    """ Language Admin """
    list_display = ('code', 'name', 'country', 'supported')
    list_display_links = ('code',)

    search_fields = ('name', 'country',)
    list_filter = ('supported',)

    #readonly_fields = ['code', ]
    list_editable = ('supported',)
    #autocomplete_fields = ['area', 'user',]

    save_on_top = True
    fieldsets = (
        ('Language', {
            'fields': ('code', 'name_en', 'country_en', 'supported', )
        }),
        ('Translations', {
            'fields': ('name_de', 'country_de',
                    'name_pt', 'country_pt',
                    'name_es', 'country_es')
        }),
    )
admin.site.register(Language, LanguageAdmin)
