from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter


from .models import Stuff, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0
    fields = ('get_edit_link', 'stuff', 'booked_from', 'booked_until', 'borrower', 'state')
    readonly_fields = ['get_edit_link',]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return format_html(
                """<a href='{url}'>{text}</a>""".format(
                url=url,
                text="Edit this %s separately" % obj._meta.verbose_name,)
            )
        return "Save and continue editing to create a link)"
    get_edit_link.short_description = "Edit link"
    get_edit_link.allow_tags = True

class StuffAdmin(admin.ModelAdmin):
    """ Stuff Admin """
    list_display = ('title', 'active', 'sharetype', 'location', 'owner',)
    list_display_links = ('title',)

    search_fields = ('title', 'description', 'country', 'city',)
    list_filter = ('sharetype', 'active',)

    readonly_fields = ['created_at', 'updated_at']
    #list_editable = ('active', 'sharetype',)
    autocomplete_fields = ['owner',]

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('owner', 'title', 'image', 'description',)
        }),
        ('Location', {
            'fields': ('country', 'city', 'street', 'longitude', 'latitude'),
        }),
        ('Flags', {
            'fields': ('active', 'sharetype', 'location_independent'),
        }),
        ('Internals', {
            'fields': ('created_at','updated_at',),
        }),
    )

    inlines = [BookingInline]

admin.site.register(Stuff, StuffAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('state', 'stuff', 'booked_from', 'booked_until', '_get_borrower', '_get_owner',)
    list_display_links = ('stuff',)
    list_editable = ('state',)

    date_hierarchy = ('updated_at')
    search_fields = ('stuff__title', 'stuff__description',)
    list_filter = ('state',)
    readonly_fields = ['created_at', 'updated_at']

    autocomplete_fields = ['borrower','stuff']

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('borrower', 'stuff', 'state',)
        }),
        ('Timeframe', {
            'fields': ('booked_from', 'booked_until',),
        }),
        ('Internals', {
            'fields': ('created_at','updated_at',),
        }),
    )

    def _get_owner(self, obj):
        return obj.stuff.owner
    _get_owner.admin_order_field  = 'stuff__owner'  #Allows column order sorting
    _get_owner.short_description = 'Owner of Stuff'  #Renames column head

    def _get_borrower(self, obj):
        return obj.borrower
    _get_borrower.admin_order_field  = 'borrower'  #Allows column order sorting
    _get_borrower.short_description = 'Borrower of Stuff'  #Renames column head
admin.site.register(Booking, BookingAdmin)
