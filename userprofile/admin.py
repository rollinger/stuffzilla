from django.contrib import admin

from .models import Profile, Location

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', )#'available', 'sharetype', 'city', 'country', 'owner',)
    #search_fields = ('title', 'available', 'description',)
    #list_filter = 'available', 'sharetype',
admin.site.register(Profile, ProfileAdmin)
