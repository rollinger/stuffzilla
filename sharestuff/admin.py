from django.contrib import admin

from .models import Stuff, Booking

class StuffAdmin(admin.ModelAdmin):
    list_display = ('title', 'available', 'sharetype', 'city', 'country', 'owner',)
    search_fields = ('title', 'available', 'description',)
    list_filter = 'available', 'sharetype',
admin.site.register(Stuff, StuffAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('stuff__name',)
    #list_filter = 'category',
admin.site.register(Booking, BookingAdmin)
