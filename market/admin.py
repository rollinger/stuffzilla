from django.contrib import admin
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.template.defaultfilters import escape
from django.utils.translation import gettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturaltime

from position.models import Address
from .models import Stuff, SharingRequest, SharingOffer


class StuffAdmin(admin.ModelAdmin):
    """ Stuff Admin """
    list_display = ('image_tag', 'title', 'sharetype', 'address', 'owner', 'active',)
    list_display_links = ('title',)

    search_fields = ('title', 'description', 'address__area__country', 'address__area__city',)
    list_filter = ('sharetype', 'active', 'location_independent')

    readonly_fields = ['created_at', 'updated_at', 'image_tag']
    list_editable = ('active',)# 'sharetype','stufftype',)
    autocomplete_fields = ['owner','address']

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('owner', 'title', 'image', 'description',)
        }),
        ('Location', {
            'fields': ('address',),
        }),
        ('Flags', {
            'fields': ('sharetype', 'active', 'location_independent'),
        }),
        ('Internals', {
            'fields': ('created_at','updated_at',),
        }),
    )

    def image_tag(self, obj):
        return u'<img src="%s" style="width:100px;"/>' % obj.image.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Stuff, StuffAdmin)

class SharingRequestAdmin(admin.ModelAdmin):
    """ SharingRequest Admin """
    list_display = ('__str__', 'callout', 'area', 'sharetype', 'stuff', '_get_share_start_ago', '_get_share_end_ago', 'user', 'active', '_get_time_ago')
    list_display_links = ('callout',)

    search_fields = ('callout', 'area__country', 'area__city',)
    list_filter = ('sharetype', 'active',)

    readonly_fields = ['created_at', 'updated_at']
    list_editable = ('active', 'sharetype',)
    autocomplete_fields = ['user','area','stuff',]

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('user', 'callout',)
        }),
        ('Search Parameters', {
            'fields': ('area', 'sharetype', 'stuff', 'share_start','share_end',),
        }),
        ('Flags', {
            'fields': ('active',),
        }),
        ('Internals', {
            'fields': ('created_at','updated_at',),
        }),
    )

    def _get_time_ago(self, obj):
        return naturaltime(obj.created_at)
    _get_time_ago.admin_order_field  = 'created_at'  #Allows column order sorting
    _get_time_ago.short_description = 'Issued'  #Renames column head

    def _get_share_start_ago(self, obj):
        return naturaltime(obj.share_start)
    _get_share_start_ago.admin_order_field  = 'share_start'  #Allows column order sorting
    #_get_share_start_ago.short_description = 'Issued'  #Renames column head

    def _get_share_end_ago(self, obj):
        return naturaltime(obj.share_end)
    _get_share_end_ago.admin_order_field  = 'share_end'  #Allows column order sorting
    #_get_share_end_ago.short_description = 'Issued'  #Renames column head

admin.site.register(SharingRequest, SharingRequestAdmin)

class SharingOfferAdmin(admin.ModelAdmin):
    """ SharingOffer Admin """
    list_display = ('_get_request_callout_link', 'pitch', '_get_stuff_area', '_get_sharetype', '_get_stufftype', '_get_time_ago', 'active',)
    list_display_links = ('pitch',)

    search_fields = ('pitch', 'stuff__area__country', 'stuff__area__city',)
    list_filter = ('stuff__sharetype', 'active',)

    readonly_fields = ['created_at', 'updated_at']
    #list_editable = ('active', 'sharetype','stufftype',)
    autocomplete_fields = ['request', 'user', 'stuff',]

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('request', 'user', 'stuff', 'pitch',)
        }),
        #('Search Parameters', {
            #'fields': ('area', 'stufftype', 'sharetype', 'stuff', 'share_start','share_end',),
        #}),
        ('Flags', {
            'fields': ('active',),
        }),
        ('Internals', {
            'fields': ('created_at', 'updated_at',),
        }),
    )

    def _get_time_ago(self, obj):
        return naturaltime(obj.created_at)
    _get_time_ago.admin_order_field  = 'created_at'  #Allows column order sorting
    _get_time_ago.short_description = 'Issued'  #Renames column head

    def _get_stuff_area(self, obj):
        return obj.stuff.address.area
    _get_stuff_area.admin_order_field  = 'stuff__address__area'  #Allows column order sorting
    _get_stuff_area.short_description = 'Area'  #Renames column head

    def _get_sharetype(self, obj):
        return obj.stuff.get_sharetype_display()
    _get_sharetype.admin_order_field  = 'stuff__sharetype'  #Allows column order sorting
    _get_sharetype.short_description = 'Sharetype'  #Renames column head

    def _get_stufftype(self, obj):
        return obj.stuff.get_stufftype_display()
    _get_stufftype.admin_order_field  = 'stuff__stufftype'  #Allows column order sorting
    _get_stufftype.short_description = 'Stufftype'  #Renames column head

    def _get_request_callout_link(self, obj):
        if obj.request:
            return format_html("""<a href='{url}' target="_blank">{callout}</a>""".format(
            url=reverse("admin:market_sharingrequest_change", args=(obj.request.id,)),
            callout=escape(obj.request.callout)))
        else:
            return None
    _get_request_callout_link.allow_tags = True
    _get_request_callout_link.admin_order_field  = 'request__callout'
    _get_request_callout_link.short_description = 'Sharing Callout'

admin.site.register(SharingOffer, SharingOfferAdmin)
