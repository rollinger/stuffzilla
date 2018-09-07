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
    list_display = ('image_tag', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('username',)
    #readonly_fields += 'image_tag'
    inlines = [UserProfileInline]

    def image_tag(self, obj):
        return u'<img src="%s" style="width:100px;"/>' % obj.user_profile.image.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

# register new user admin that includes a UserProfile
admin.site.register(User, ProfileUserAdmin)
