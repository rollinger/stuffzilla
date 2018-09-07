from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . models import Profile


# unregister old user admin
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False

class ProfileUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# register new user admin that includes a UserProfile
admin.site.register(User, ProfileUserAdmin)
