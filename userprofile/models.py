from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from django.contrib.auth.models import User



class LocationManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Location(models.Model):
    """
    Location holding the geo location of an object.
    most notably from Model: User, Stuff (related_name = location_owner)
    """

    country     = models.CharField(_('Country'), max_length=255, null=True, blank=True)
    city        = models.CharField(_('City'), max_length=255, null=True, blank=True)
    street      = models.CharField(_('Street'), max_length=255, null=True, blank=True)
    longitude   = models.FloatField(_('GPS Longitude'),null=True, blank=True)
    latitude    = models.FloatField(_('GPS Latitude'), null=True, blank=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = LocationManager

    @property
    def address(self):
        return "%s, %s, %s," % locals(self.street,self.city,self.country)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')



class ProfileManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Profile(models.Model):
    """ Profile holding additional information for a user """
    user            = models.OneToOneField(User,
                        help_text=_('User Account of this Profile'),
                        on_delete=models.PROTECT, related_name="user_profile")

    location        = models.OneToOneField(Location,
                        help_text=_('Address of your User Account'),
                        on_delete=models.PROTECT, related_name="location_owner")

    phone_number    = models.CharField(_('Phone Number'),
        help_text=_('Your phone number to reach out to you.'),
        validators=[ RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))],
        max_length=17, blank=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = ProfileManager

    def __str__(self):
        return "%s's Profile" % (self.user.name)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
