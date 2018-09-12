from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Language(models.Model):
    """ Maps the config Language setting and allows for Language Selection """
    # O    TODO [version 0.]: Add Flag icon to Language Model
    code     = models.CharField(_('Language Code'),
                help_text=_('Standard language code representation. Ex.: en_AU'), max_length=10)

    name     = models.CharField(_('Language Name'),
                help_text=_('Name of the Language. Ex.: English'), max_length=100)

    country  = models.CharField(_('Country'),
                help_text=_('Name of the Country. Ex.: Australia'), max_length=100, null=True, blank=True)

    supported    = models.BooleanField(_("Translation supported"),
                help_text=_('If the language is supported in the App Translation Sytem'), default=False)

    def __str__(self):
        """ Returns the language code """
        return "%s" % (self.code,)

    # O    TODO [version 0.]:   Check in save if supported = True that the code is present in the config.LANGUAGE Settings

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Language')
        ordering = ['name','country']



class AreaManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Area(models.Model):
    """
    An Area defines an urban area (such as a city) in a Region in a Country. Many assets link to instances of this model for search and retrieval based on geographic proximity. The verified flag means that it is an official Area.
    """
    country     = models.CharField(_('Country'),
                help_text=_('Country the Area is located in.'),
                max_length=255)
    region      = models.CharField(_('Region'),
                help_text=_('Region the Area is located in.'),
                max_length=255, null=True, blank=True)
    # O    TODO [version 0.]: Integrate the concept of Municipality and County into Area Model. E.g. Portugal => Grande Porto => Porto
    city        = models.CharField(_('City'),
                help_text=_('City the Area is located in.'),
                max_length=255)
    verified    = models.BooleanField(_("Verified Area"),
                help_text=_('If the specified area is verified to be existent and relevant'), default=False)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = AreaManager

    def __str__(self):
        """ Returns the city and the country """
        return "%s (%s)" % (self.city, self.country)

    class Meta:
        verbose_name = _('Area')
        verbose_name_plural = _('Areas')
        ordering = ['country','city']

        #unique_together = ['city','region','country']

        # O    TODO [version 0.5]: Add Db Indexes on cities so retrieval is faster https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []



class AddressManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Address(models.Model):
    """
    An Address combines an Area with a specific Address. Many assets link to instances of this model for locating those to a specific geographic Address
    """

    street          = models.CharField(_('Street'),
                    help_text=_('Street Name'), max_length=255)
    street_number   = models.CharField(_('Street Number'),
                    help_text=_('House Number'), max_length=55)
    supplement      = models.CharField(_('Address Supplements'),
                    help_text=_('Additional Information (Appartment Number,...)'), max_length=255, null=True, blank=True)
    zipcode         = models.CharField(_('Zip Code'),
                    help_text=_('Area Code'), max_length=55, null=True, blank=True)
    area            = models.ForeignKey(Area,
                    help_text=_('Owner of the Item or Service'),
                    related_name="addresses", on_delete=models.PROTECT)
                    # If an Area has Addresses first those addresses need to be deleted before deleting the Area itself
    # Creator of the Address
    # O    TODO [version 0.]: Weird with profile FK... BUG?
    user       = models.ForeignKey(User,
                help_text=_('User creating the Address'), null=True, blank=True,
                related_name="addresses", on_delete=models.PROTECT)
    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = AddressManager

    @property
    def city(self):
        return self.area.city

    @property
    def country(self):
        return self.area.country

    @property
    def region(self):
        return self.area.region

    @property
    def full_street(self):
        """ Returns the full street information """
        if self.supplement:
            return "%s %s (%s)" % (self.street, self.street_number, self.supplement)
        else:
            return "%s %s" % (self.street, self.street_number)

    @property
    def full_area(self):
        """ Returns the full area information, excluding the region """
        if self.zipcode:
            return "%s %s (%s)" % (self.zipcode, self.city, self.country)
        else:
            return "%s (%s)" % (self.city, self.country)

    def __str__(self):
        """ Returns the Address """
        return "%s; %s" % (self.full_street, self.full_area)


    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        ordering = ['street','street_number']

        # O    TODO [version 0.]: unique together user & __str__ (or subset) [no user should have 2 of the same addresses] Overkill?

        # O    TODO [version 0.5]: Add Db Indexes on street and number so retrieval is faster https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []
