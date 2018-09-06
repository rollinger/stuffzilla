from django.contrib import admin

from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    """ Stuff Admin """
    list_display = ('title', 'image_tag', 'person_name', 'published',)
    list_display_links = ('title',)

    search_fields = ('title', 'content', 'person_name',)
    list_filter = ('published',)

    readonly_fields = ['created_at', 'updated_at', 'image_tag',]
    list_editable = ('published',)

    save_on_top = True
    fieldsets = (
        ('General', {
            'fields': ('title', 'content')
        }),
        ('Person', {
            'fields': ('person_name', 'person_image', 'image_licence'),
        }),
        ('Flags', {
            'fields': ('published',),
        }),
        ('Internals', {
            'fields': ('created_at','updated_at',),
        }),
    )

    def image_tag(self, obj):
        return u'<img src="%s" style="width:100px;"/>' % obj.person_image.url
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

admin.site.register(Testimonial, TestimonialAdmin)
